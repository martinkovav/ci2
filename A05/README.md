# CDXML to PNG converter

This repository contains a script `cdx2png.py` that creates a set of .png (graphic) files from a set of *.cdxml (ChemDraw) files. The script looks for CDXML file names in command line arguments (extension symbols are allowed). The resulting PNG files will have the same name base as CDXML files, only with different extensions. Additionaly, the script finds two molecules among the converted molecules - the first with the lowest relative molecular weight (Mr), the second with the largest Mr, and prints them (their file names) together with the Mr to the standard output.

# Instructions to clone, set up, and run the script

## Clone the repository
```
git clone https://github.com/martinkovav/ci2.git
cd ci2/A05
```

## Create virtual environment
```
python3 -m venv venv
source venv/bin/activate
```
## Install required packages
```
pip3 install rdkit
pip3 install openbabel-wheel
```
## Run the script
```
python3 cdx2png.py *.cdxml
```

This will create .png files for each .cdxml file and prints the lowest and highest Mr.