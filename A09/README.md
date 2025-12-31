# Flask ChEMBL SMILES Lookup

This repository contains a small Flask web application that accepts a chemical structure in SMILES format, queries the ChEMBL web service (via the chembl_webresource_client Python package) for matching compounds, extracts the first compound from the result, and displays the compound information in a user-friendly web page (name, ChEMBL ID, Molecular structure image, Molecular formula, canonical SMILES, database link and molecular weight). The app also allows repeated queries from the same page.

# Instructions to clone, set up, and run the script

## Clone the repository

```bash
git clone https://github.com/martinkovav/ci2.git
cd ci2/A08
```

## Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

## Install required packages
```bash
pip3 install Flask
pip3 install chembl_webresource_client
```

## Run (debug)
```bash
export FLASK_APP=app.py
flask run
```
* Running on http://127.0.0.1:5000

## How to use the web page
Enter SMILES String:

Example SMILES: O=C(O)c1ccccc1C(=O)O

Expected output:

PHTHALIC ACID

ChEMBL ID: CHEMBL1045

Molecular Structure

...

Canonical SMILES

O=C(O)c1ccccc1C(=O)O

Molecular Formula

C8H6O4

Molecular Weight

166.13 g/mol

Database Link

View on ChEMBL →