# Librairies
import osxphotos
import json
import os



# Charger la photothèque par défaut
photosdb = osxphotos.PhotosDB()

# Récupérer toutes les photos
photos = photosdb.photos()

# Création liste des métadonnées valides
photos_metadata = []

## Définir le chemin absolu du projet
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_data_folder = os.path.join(project_root, "data", "photos_metadata_json")

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_data_folder, exist_ok=True)

# Parcourir les photos et extraire les métadonnées de celles qui possèdent des données GPS
for photo in photos:
    if photo.latitude is not None and photo.longitude is not None :
        
        file_path = os.path.join(output_data_folder, f"{photo.original_filename}_metadonnees.json")

        # Remplissage de la liste des métadonnes 
        photos_metadata = [{
            "nom": photo.original_filename, 
            "date": str(photo.date).split(" ")[0],  # Extraire uniquement la date (sans l'heure)
            "latitude": round(photo.latitude, 5),  # Arrondir à 5 décimales
            "longitude": round(photo.longitude, 5)
        }]
        # Écriture des métadonnées dans un fichier JSON
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(photos_metadata, f, indent=4, ensure_ascii=False)

print(f"\nDonnées enregistrées dans le dossier {os.path.basename(output_data_folder)} avec succès !\n")