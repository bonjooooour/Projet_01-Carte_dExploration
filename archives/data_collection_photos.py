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

# Chemin de stockage
data_folder = "PROJET 01 - Carte d'exploration/data"
chemin_fichier = os.path.join(data_folder, "photos_metadonnees.json")

# Création du dossier s'il n'existe pas
os.makedirs(data_folder, exist_ok=True)  

# Parcourir les photos et extraire les métadonnées de celles qui possèdent des données GPS
for photo in photos:
    if photo.latitude is not None and photo.longitude is not None :
        # Remplissage de la liste des métadonnes 
        photos_metadata.append({
            "nom": photo.original_filename, 
            "date": str(photo.date).split(" ")[0],  # Extraire uniquement la date (sans l'heure)
            "latitude": round(photo.latitude, 5),  # Arrondir à 5 décimales
            "longitude": round(photo.longitude, 5)
        })

# Écriture des métadonnées dans un fichier JSON
with open(chemin_fichier, "w", encoding="utf-8") as f:
    json.dump(photos_metadata, f, indent=4, ensure_ascii=False)

print("\nDonnées enregistrées dans photos_metadonnees.json avec succès !\n")