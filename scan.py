import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename", help= "indiquer le nom du fichier")
parser.add_argument("extension", default="py", help="indiquer le type de dossier qu'on ouvre")
args = parser.parse_args()
FILENAME = args.filename
EXT = args.extension

from pathlib import Path
from datetime import datetime as DateTime


def scan(FILENAME, EXT):
    p= sorted(Path(FILENAME).glob('*.' + EXT))
    for file in p:
        print(file.resolve())
        print(file.stat().st_size())
        dt= DateTime.fromtimestamp(file.stat().st_mtime)
        print(f"la date est {dt}")
        with open(str(file)) as f:
            print(f.readline())

#cette version ne marche pas avec tous les fichiers je n'arrive pas mieux
#ce travail a ete effectue en collaboration avec Armand Bourderioux