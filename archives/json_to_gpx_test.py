# Librairies
import os
import json
import gpxpy
import gpxpy.gpx

# Définir les chemins d'entrée et de sortie
input_file = "/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/photos_metadata_json/_MG_3441.JPG_metadonnees.json"
output_file = "/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/photos_locations.gpx"

# Vérifier que le fichier d'entrée existe
if not os.path.exists(input_file):
    raise FileNotFoundError(f"Le fichier {input_file} n'existe pas")

# Fonction pour convertir JSON en GPX
def json_to_gpx(json_file_path, gpx_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    gpx = gpxpy.gpx.GPX()
    gpx_track = gpxpy.gpx.GPXTrack()
    gpx.tracks.append(gpx_track)
    gpx_segment = gpxpy.gpx.GPXTrackSegment()
    gpx_track.segments.append(gpx_segment)
    
    point = gpxpy.gpx.GPXTrackPoint(
        latitude=data['latitude'],
        longitude=data['longitude'],
        time=data['date']
    )
    gpx_segment.points.append(point)
    
    with open(gpx_file_path, 'w', encoding='utf-8') as f:
        f.write(gpx.to_xml())

# Conversion en GPX
json_to_gpx(input_file, output_file)

print(f"Conversion terminée. Fichier GPX créé : {output_file}")