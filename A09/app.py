from flask import Flask, render_template, request, jsonify, url_for
from flask_cors import CORS
from chembl_webresource_client.new_client import new_client
import os
import subprocess

app = Flask(__name__)
CORS(app)
molecule = new_client.molecule

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def api_search():
    data = request.get_json()
    smiles = data.get('smiles', '').strip()
    if not smiles:
        return jsonify({'error': 'Please provide a SMILES string.'}), 400

    try:
        # Query ChEMBL
        search_res = molecule.filter(molecule_structures__canonical_smiles=smiles)
        search_list = list(search_res)
        if not search_list:
            return jsonify({'error': 'No results found for the given SMILES.'}), 404

        first = search_list[0]
        result = {
            'chembl_id': first.get('molecule_chembl_id'),
            'pref_name': first.get('pref_name'),
            'canonical_smiles': first.get('molecule_structures', {}).get('canonical_smiles'),
            'formula': first.get('molecule_properties', {}).get('full_molformula'),
            'mol_wt': first.get('molecule_properties', {}).get('full_mwt'),
            'synonyms': [s['molecule_synonym'] for s in first.get('synonyms', [])],
        }

        # Generate 3D image
        img_dir = os.path.join("static", "img")
        pov_file = 'molecule.pov'
        png_file = 'molecule.png'

        # Generate POV from SMILES
        subprocess.run(['obabel', f'-:{smiles}', '-opov', '-O', pov_file, '--gen3D'], check=True, cwd=img_dir)

        # Generate PNG with povray
        subprocess.run(['povray', pov_file], check=True, cwd=img_dir)

        os.remove(os.path.join(img_dir, pov_file))

        result['image_url'] = url_for('static', filename=os.path.join("img", png_file))

        return jsonify(result)

    except Exception as e:
        return jsonify({'error': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)