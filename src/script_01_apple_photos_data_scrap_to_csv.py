"""
Fichier : script_01_apple_photos_data_scrap_to_csv.py

- Collecte locale des métadonnées des photos stockées dans la librairie de l'application Apple Photos (MacOS)
- Pour les photos disposant de données de localisation, stockage dans un fichier CSV sous le format : 
    |   nom     |    date    |   latitude    |   longitude   |
"""



### Librairies ###
import osxphotos
import pandas as pd
from datetime import datetime



### nom du fichier CSV ###
CSV_FILE_NAME = "apple_photos_librairy_metadata_"+str(datetime.now().date())+".csv"



### Fonction unique ###

def main_01(output_folder):
    # Utilisation du module OSPhotos pour accéder à la photothèque locale Apple
    photosdb = osxphotos.PhotosDB()
    photos = photosdb.photos()

    count = 0           # Compteur
    data = []           # Création d'une liste où stocker les données valides

    # Passage en revue de toutes les photos
    for photo in photos:
        count += 1
        
        # Sélection des éléments possédant des données de localisation
        if photo.latitude is not None and photo.longitude is not None :
            data.append(
                {
                    "nom": photo.original_filename,
                    "date": str(photo.date).split(" ")[0],      # Extraire uniquement la date (sans l'heure)
                    "latitude": round(photo.latitude, 5),       # Arrondir à 5 décimales
                    "longitude": round(photo.longitude, 5)
                }
            )

    # Sauvegarde du dataframe dans un CSV
    df = pd.DataFrame(data)
    df.to_csv(output_folder + "/" + CSV_FILE_NAME, index=False, encoding="utf-8")
    print(f"\n{count} éléments passés en revue.\n")
    print("Fichier CSV normalisé, contenant les données de position photographiques généré avec succès !")
