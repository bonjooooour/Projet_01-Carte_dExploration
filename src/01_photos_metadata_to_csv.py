"""
01_photos_metadata_to_csv.py 

- Collecte locale des métadonnées des photos de l'application Apple Photos 
- Pour les photos disposant de données de localisation, stockage [nom, date, longitude, latitude] dans un fichier CSV
"""


### Librairies ###
import osxphotos
import pandas as pd


### Utilisation du module OSXPhotos ###

# Charger la photothèque Photos
photosdb = osxphotos.PhotosDB()
# Récupérer une seule photo (par exemple, la plus récente)
photos = photosdb.photos()


### Passage en revue de toutes les photos ###

count = 0   # Compteur
data = []   # Création d'une liste où stocker les données valides

for photo in photos:
    count += 1
    # Sélection des éléments avec des données de positions
    if photo.latitude is not None and photo.longitude is not None :
        data.append(
            {
                "nom": photo.original_filename,
                "date": str(photo.date).split(" ")[0],  # Extraire uniquement la date (sans l'heure)
                "latitude": round(photo.latitude, 5),   # Arrondir à 5 décimales
                "longitude": round(photo.longitude, 5)
            }
        )


### Création du dataframe pour stockage des données dans un CSV ###

# Emplacement de sauvegarde & nom du fichier CSV
csv_file_name = "photos_metadata.csv"
output_folder = "/Users/mgerenius/VScode Workspace/PROJET 01 - Carte d'exploration/data/CSV_files"

# Sauvegarde du dataframe dans un CSV
df = pd.DataFrame(data)
df.to_csv(output_folder + "/" + csv_file_name, index=False, encoding="utf-8")
print(f"\n{count} éléments passés en revue.\n")
print("Fichier CSV généré avec succès !")