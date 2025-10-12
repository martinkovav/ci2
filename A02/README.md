texter.py

This repository contains a simple Python script that analyzes a text file and prints:
    The number of paragraphs in the text.
        → A paragraph is defined as a block of text separated by a blank line.
    The number of space characters (" ") that appear immediately after a dot (". ").

Project Files
texter.py – the main Python script
test.txt – example input file for testing

How It Works
    (a) Paragraph Counting
        Paragraphs are counted as blocks of text separated by blank line.
    (b) Spaces After Dots
        The script counts how many times a space character directly follows a dot.

Instructions to Clone and Run

Clone the repository:
git clone https://github.com/martinkovav/ci2.git
cd ci2/A02

Ensure Python 3 is installed:
python3 --version

Usage:
python3 texter.py <file_name>

Example
Run the script with the test file:
python3 texter.py test.txt

Expected output:
Number of paragraphs: 5
Number of spaces immediately after a dot: 43