# Librairies
import os
import pandas as pd
from gpx_converter import Converter

"""
/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/photos_metadata_json
/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/photos_metadata_gpx
"""


# Définir les chemins d'entrée et de sortie
# input_folder_json = input("Renseigner le chemin du dossier d'entrée contenant les fichiers JSON : ")
# output_folder_gpx = input("Renseigner le chemin du dossier de sortie qui stockera les fichiers GPX : ")
input_folder_json = "/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/photos_metadata_json"
output_folder_gpx = "/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/photos_metadata_gpx"

# Création du dossier de sortie s'il n'existe pas déjà
os.makedirs(output_folder_gpx, exist_ok=True)

# Compteur de fichiers convertis
count = 0

# Passage en revue et conversion des fichiers JSON en GPX
for file in os.listdir(input_folder_json):
    
    # Sélection des fichiers JSON
    if file.endswith(".json"):
        count += 1
        json_file_path = os.path.join(input_folder_json, file)
        gpx_file_path = os.path.join(output_folder_gpx, file.replace('.json', '.gpx'))
        # Création du convertisseur avec le fichier JSON 
        converter = Converter(input_file=json_file_path)
        # Conversion en GPX
        converter.json_to_gpx(
            output_file=gpx_file_path,
            lats_colname="latitude",
            longs_colname="longitude"
        )

print(f"{count} fichiers on bien été convertis au format GPX.")