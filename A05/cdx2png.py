import sys
import os
from rdkit import Chem
from rdkit.Chem import Draw, Descriptors
from openbabel import openbabel

class ChemDraw2png:

    def __init__(self, cdxml_files):
        self.cdxml_files = cdxml_files
    
    # converts .cdxml file to .mol using Open Babel
    def convert_cdxml_to_mol(self, cdxml_file):
        # create converter
        conv = openbabel.OBConversion()
        conv.SetInAndOutFormats("cdxml", "mol")

        mol = openbabel.OBMol()
        conv.ReadFile(mol, cdxml_file)
        
        mol_file = cdxml_file.replace(".cdxml", ".mol")
        conv.WriteFile(mol, mol_file)
        return mol_file

    def mol_to_png(self, mol_file):
        # use RDkit to read .mol file and convert to .png
        mol = Chem.MolFromMolFile(mol_file, sanitize=False)
        
        # create png file
        png_file = mol_file.replace(".mol", ".png")
        Draw.MolToFile(mol, png_file)
        return mol, png_file

    def process_files(self):
        mol_weights = []

        for cdxml_file in self.cdxml_files:
            mol_file = self.convert_cdxml_to_mol(cdxml_file)
            mol, png_file = self.mol_to_png(mol_file)
            
            mw = Descriptors.MolWt(mol)
            mol_weights.append((cdxml_file, mw))
            # print molecular weight
            print(f"Converted {cdxml_file} → {png_file} (Mr = {mw:.2f})")
            os.remove(mol_file)

        if mol_weights:

            # find min and max molecular weights
            min_mol = min(mol_weights, key=lambda x: x[1])
            max_mol = max(mol_weights, key=lambda x: x[1])

            # print summary including compound names
            print("\n=== Summary ===")
            print(f"Lowest Mr:  {min_mol[0]} (Mr = {min_mol[1]:.2f})")
            print(f"Highest Mr: {max_mol[0]} (Mr = {max_mol[1]:.2f})")

if __name__ == "__main__":
    c2p = ChemDraw2png(sys.argv[1:])
    c2p.process_files()