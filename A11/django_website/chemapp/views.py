from django.shortcuts import render

import os # path, remove
import subprocess # run
from chembl_webresource_client.new_client import new_client

from .models import Smiles

# Create your views here.
def index(request):
    return render(request, 'chemapp/index.html')

def chembl(request):
    context = {}
    if request.method == 'GET' and 'smiles' in request.GET:
        smiles = request.GET['smiles']

        # save smiles to database
        Smiles(smiles_text=smiles).save()

        # query ChEMBL
        molecule = new_client.molecule
        search_res = molecule.filter(molecule_structures__canonical_smiles=smiles)
        if search_res:
            first = list(search_res)[0]
            molecule = {}
            molecule['smiles'] = smiles
            molecule['chembl_id'] = first.get('molecule_chembl_id')
            molecule['pref_name'] = first.get('pref_name')
            molecule['formula'] = first.get('molecule_properties', {}).get('full_molformula')
            molecule['mol_wt'] = first.get('molecule_properties', {}).get('full_mwt')
            molecule['synonyms'] = [s['molecule_synonym'] for s in first.get('molecule_synonyms', [])]

            context['molecule'] = molecule
        else:
            context['error'] = f'No results found for "{smiles}".'

    return render(request, 'chemapp/chembl.html', context)

def povray(request):
    context = {}
    if request.method == 'GET' and 'smiles' in request.GET:
        smiles = request.GET['smiles']

        img_dir = os.path.join('chemapp', 'static', 'chemapp', 'images')
        pov_file = 'molecule.pov'
        png_file = 'molecule.png'

        # create .pov file from smiles using obabel
        subprocess.run(['obabel', f'-:{smiles}', '-opov', '-O', pov_file, '--gen3D'], check=True, cwd=img_dir)
        # create image of molecule described in .pov file using povray
        subprocess.run(['povray', pov_file], check=True, cwd=img_dir)
        # delete intermediate .pov file
        os.remove(os.path.join(img_dir, pov_file))

        context['smiles'] = smiles
        context['image_url'] = os.path.join('chemapp', 'images', png_file)

    return render(request, 'chemapp/povray.html', context)