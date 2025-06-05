"""
Fichier : script_02_strava_activities_data_to_csv.py

Conversion des données d'activités Strava en fichiers CSV normalisés :
- Passe en revue l'entièreté des fichiers présents dans une archive Strava 
    (préalablement exportée depuis mon compte personnel)
- Si le fichier possède l'extension .gpx : conversion au format CSV puis formatage
- Si le fichier possède l'extension .gz : dezippage vers fichier .fit, conversion en CSV puis formatage
- Formatage en CSV sous le format :
    |   nom     |    date    |   latitude    |   longitude   |
"""



### Librairies ###
import os
import gzip
import shutil
import pandas as pd
from fitparse import FitFile
from gpx_converter import Converter



# ### Chemins d'accès ###
# INPUT_FOLDER = "/Users/mgerenius/VScode_Workspace/Projet_01-Carte_dExploration/data/Strava_RAW_files/activities"
# OUTPUT_FOLDER = "/Users/mgerenius/VScode_Workspace/Projet_01-Carte_dExploration/data/CSV_files"



### Fonctions ###


# 1 # Fichiers .gz & .fit

def unzip_gz_to_fit(file, input_folder):
    """
    Dézippe un fichier .fit.gz en fichier .fit pour l'enregistrer dans son dossier d'origine.

    param :
    - file : fichier à dézipper
    - input_folder : dossier d'origine

    sortie :
    - fichier dézippé
    """
    file_name = os.path.basename(file)                          # Récupération du nom du fichier
    output_file = os.path.join(input_folder, file_name[:-3])    # Retire ".gz" de l'extension

    # Dézippe du fichier .gz passé en revue
    with gzip.open(file, 'rb') as f_in, open(output_file, 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)

    return output_file


def fit_to_csv(file, output_folder):
    """
    Convertit un fichier FIT en CSV.

    param :
    - file : fichier FIT à convertir
    - output_folder : dossier de sortie

    sortie :
    - chemin du fichier CSV créé
    """
    fitfile = FitFile(file)
    data_list = []

    # Extraction des enregistrements principaux vers une liste
    for record in fitfile.get_messages("record"):
        record_data = {}
        for field in record:
            if field.name == 'position_lat' and field.value is not None:
                record_data['position_lat'] = field.value / ((2**32) / 360)
            elif field.name == 'position_long' and field.value is not None:
                record_data['position_long'] = field.value / ((2**32) / 360)
            else:
                record_data[field.name] = field.value
        data_list.append(record_data)

    # Conversion
    file_name = os.path.basename(file)
    csv_file_name = file_name.replace(".fit", ".csv")
    output_file = os.path.join(output_folder, csv_file_name)

    # Création d'un dataframe et sauvegarde au format CSV
    df = pd.DataFrame(data_list)
    df.to_csv(output_file, index=False, encoding="utf-8")

    return output_file


def fit_csv_normalizer(file, output_folder):
    """
    Normalise un fichier CSV anciennement FIT, sous le format :
    |   nom     |    date    |   latitude    |   longitude   |

    param :
    - file : fichier CSV non normalisé
    - output_folder : dossier de sortie

    sortie :
    - file_name : nom du fichier qui a été normalisé
    """
    df = pd.read_csv(file)
    file_name = os.path.basename(file)

    data_list = []
    count = 0
    for row in df.itertuples():
        if pd.notnull(row.position_lat) and pd.notnull(row.position_long):
            count += 1
            date, _ = row.timestamp.split(' ', 1)
            data_list.append({
                "nom": file_name + str(count),
                "date": date,
                "latitude": row.position_lat,
                "longitude": row.position_long
            })

    # Stockage dans un dataframe & enregistrement au format CSV
    new_df = pd.DataFrame(data_list)
    new_df.to_csv(file, index=False, encoding="utf-8")  # On écrase la version du CSV non-normalisée

    return file_name


# 2 # Fichiers .gpx

def gpx_to_csv(file, output_folder):
    """
    Convertit un fichier GPX en CSV.

    param :
    - file : fichier d'entrée à convertir
    - output_folder : dossier de stockage du fichier

    sortie :
    - fichier converti au format CSV
    """
    # Vérifier et créer le dossier de sortie si nécessaire
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Extraire le nom du fichier sans l'extension
    file_name = os.path.basename(file)
    csv_file_name = file_name.replace(".gpx", ".csv")
    output_file = os.path.join(output_folder, csv_file_name)

    # Conversion du fichier GPX en CSV
    Converter(input_file=file).gpx_to_csv(output_file=output_file)

    return output_file


def gpx_csv_normalizer(file):
    """
    Normalise un fichier CSV anciennement GPX, sous le format :
    |   nom     |    date    |   latitude    |   longitude   |

    param :
    - file : fichier CSV non normalisé

    sortie :
    - file_name : nom du fichier qui a été normalisé
    """
    df = pd.read_csv(file)
    file_name = os.path.basename(file)

    data_list = []
    count = 0

    # Itération sur chaque ligne du fichier et collecte des données dans une liste
    for row in df.itertuples():
        count += 1
        date, _ = row.time.split(' ', 1)
        data_list.append({
            "nom": file_name + str(count),
            "date": date,
            "latitude": row.latitude,
            "longitude": row.longitude
        })

    # Conversion de la liste en dataframe
    new_df = pd.DataFrame(data_list)
    new_df.to_csv(file, index=False, encoding="utf-8")

    return file_name



### Fonction principale ###

def main_02(input_folder, output_folder):
    """
    Fonction principale qui orchestre la conversion et la normalisation des fichiers Strava.

    params :
    - input_folder : dossier contenant les fichiers brutes (.gpx & .fit.gz)
    - output_folder : dossier de destination des fichiers CSV normalisés
    """
    gpx_counter = 0
    fit_counter = 0
    global_counter = 0

    for file in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file)

        # Cas où il s'agit d'un fichier GPX
        if file.endswith('.gpx'):
            gpx_counter += 1
            # Conversion en CSV et sauvegarde dans le dossier indiqué
            csv_file_from_gpx = gpx_to_csv(file_path, output_folder)
            # Formatage du fichier selon la norme souhaitée
            normalize_csv_from_gpx = gpx_csv_normalizer(csv_file_from_gpx)

        # Cas où il s'agit d'un fichier .fit.gz
        elif file.endswith(".gz"):
            fit_counter += 1
            # Dézippage du fichier .gz
            unzip_fit_file_from_gz = unzip_gz_to_fit(file_path, input_folder)
            # Conversion en CSV et sauvegarde dans le dossier indiqué
            csv_file_from_fit = fit_to_csv(unzip_fit_file_from_gz, output_folder)
            # Formatage du fichier selon la norme souhaitée
            normalize_csv_from_fit = fit_csv_normalizer(csv_file_from_fit, output_folder)

        # Compteur global
        global_counter +=1 
        print(f"Nombre de fichiers STRAVA traités : {global_counter}")
    
    print(f"\n{gpx_counter} fichiers GPX et {fit_counter} fichiers FIT ont été convertis et formatés au format CSV.")
