# Django Chemistry website

A simple Django web application for retrieving and visualizing information about molecules. The desired molecule is specified using the **SMILES** format. The website has two pages:

### ChEMBL
Get information about the molecule from the ChEMBL database. The information: CheMBL id, preferred name, formula, molecular weight and list of synonyms.

### Povray
Get an image of the 3D structure of the molecule. The image is generated using Povray.

## Instructions for running the app

### Clone the repository

```bash
git clone https://github.com/martinkovav/ci2.git
cd ci2/A11
```

### Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install required packages
```bash
brew install povray
brew install open-babel
pip3 install Django
pip3 install chembl_webresource_client
```

### Run (debug)
```bash
cd django_website
python3 manage.py runserver
```
Running on http://127.0.0.1:8000
