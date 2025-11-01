import sys
from bs4 import BeautifulSoup

# check command line argument count
if len(sys.argv) < 2:
    # the parameter (file name) is not specified, print help on how to use the script
    print("Usage: python3 molbase_parser.py <html_file>")
    sys.exit(1)

# assign file_name
file_name = sys.argv[1]

try:
    with open(file_name, "r", encoding="utf-8") as f:
        html = f.read()
except FileNotFoundError:
    print(f"File not found: {file_name}")
    sys.exit(2)

soup = BeautifulSoup(html, "html.parser")

# Find all <h3> elements and print the value of their "title" attribute, one per line.
for h3 in soup.find_all("h3"):
    title = h3.get("title")
    if title:
        print(title.strip())
