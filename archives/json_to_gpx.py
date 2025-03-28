import os
import pandas as pd
from gpx_converter import Converter

# Définir les chemins d'entrée et de sortie
input_file = "/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/photos_metadata_json/_MG_3441.JPG_metadonnees.json"
output_file = "/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/photos_locations.gpx"

# Vérifier que le fichier d'entrée existe
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Le fichier {input_file} n'existe pas")

# Création du convertisseur avec le fichier JSON source
converter = Converter(input_file=input_file)

# Conversion en GPX
converter.json_to_gpx(
    output_file=output_file,
    lats_colname="latitude",
    longs_colname="longitude"
)

print(f"Conversion terminée. Fichier GPX créé : {output_file}")
