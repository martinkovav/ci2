from flask import Flask, render_template, request
from chembl_webresource_client.new_client import new_client

app = Flask(__name__)
molecule = new_client.molecule
image = new_client.image

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    error = None
    smiles = ''
    if request.method == 'POST':
        smiles = request.form.get('smiles', '').strip()
        if smiles:
            try:
                # Try searching; you could use .search or .filter depending on API version
                search_res = molecule.filter(molecule_structures__canonical_smiles=smiles)
                search_list = list(search_res)
                if search_list:
                    first = search_list[0]
                    # extract useful fields
                    result = {
                        'chembl_id': first.get('molecule_chembl_id'),
                        'pref_name': first.get('pref_name'),
                        'canonical_smiles': first.get('molecule_structures', {}).get('canonical_smiles'),
                        'formula': first.get('molecule_properties', {}).get('full_molformula'),
                        'mol_wt': float(first.get('molecule_properties', {}).get('full_mwt')),
                        'synonyms': first.get('synonyms', []),
                        'raw': first
                    }

                    # Get molecule image as SVG
                    try:
                        image.set_format('svg')
                        svg_data = image.get(result['chembl_id'])
                        result['molecule_image'] = svg_data
                    except Exception as img_error:
                        result['molecule_image'] = None

                else:
                    error = 'No results found for the given SMILES.'

            except Exception as e:
                error = f'Error querying ChEMBL: {e}'
        else:
            error = 'Please provide a SMILES string.'

    return render_template('index.html', result=result, error=error, smiles=smiles)

if __name__ == '__main__':
    app.run(debug=True)