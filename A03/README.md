# MolBase benzidine parser

This repository contains a small parser `molbase_parser.py` that extracts compound names from a MolBase search-results page (first page for the query "benzidine"). The script prints, one per line, the value of the `title` attribute of each `<h3>` element found in the provided HTML file.

# Instructions to clone, set up, and run the script

## Clone the repository
git clone https://github.com/martinkovav/ci2/A03.git
cd martinkovav/ci2/A03

## Install required packages
pip3 install beautifulsoup4

## Save the MolBase search results page
1. Go to https://www.molbase.com and search for "benzidine".
2. Open the first search-results page (the page listing hits).
3. Save the page from your browser as HTML (File → Save As → "Webpage, HTML only").
4. Name the file `molbase_benzidine.html` and put it into this `A03/` folder.

## Run the parser
python3 molbase_parser.py molbase_benzidine.html

This will print each found title attribute from <h3> elements, one per line.