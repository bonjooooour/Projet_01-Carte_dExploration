"""
Fichier : script_03_multiple_to_one_csv.py

Fusionne les multiples fichiers CSV préalablement générés, pour n'en avoir plus qu'un unique, normalisé.

- Vérifie si un fichier est vide pour l'écarter
- Agrège les fichiers CSV en un seul et unique
- Normalise au format : 
    |   nom     |    date    |   latitude    |   longitude   |
"""



### Librairies ###
import os
import pandas as pd
from datetime import datetime



### Nom du fichier CSV ###
UNIFIED_CSV_FILE_NAME = "unified_&_normalized_dataframe_"+str(datetime.now().date())+".csv"



### Fonctions ###

# Vérification d'éventuels fichiers vides
def file_is_empty(file):
    """
    Vérifie si un fichier est vide : taille < 5 octets

    param:
    - file : fichier inspecté

    sortie : 
    - True : booléen, si le fichier est bien vide
    """
    if os.path.getsize(file) < 5:
        return True


# Fusion des multiples fichiers en un unique CSV
def multiple_to_one_csv(input_folder, output_folder):
    """
    Fusionne l'ensemble des fichiers CSV pour n'en former plus qu'un seul
    
    param:
    - input_folder : emplacement des multiples fichiers CSV
    
    sortie : 
    - one_csv : fichier CSV unique
    """
    # Création du dossier de sotie si non existant
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    df_list = []        # Création d'une liste vide pour y stocker chaque df

    # itération de l'ensemble des fichiers
    for element in os.listdir(input_folder):
        file = os.path.join(input_folder, element)      # "file" = chemin d'accès complet du fichier
        # Vérification que le fichier inspecté n'est pas vide
        if not file_is_empty(file):
            # Stockage des données dans un dataframe, puis ajout à la liste
            df = pd.read_csv(file, encoding='utf-8')
            df_list.append(df)

    # Création et sauvegarde du CSV final
    unified_csv_file = os.path.join(output_folder, UNIFIED_CSV_FILE_NAME)   # Chemin d'accès complet du fichier final
    pd.concat(df_list).to_csv(unified_csv_file)

    return unified_csv_file


# Normalisation du fichier CSV unique généré
def dataframe_normalizer(unified_csv_file):
    """ 
    Formatage du CSV unique sous le format :
    |   nom     |    date    |   latitude    |   longitude   |

    param :
    - fichier à normaliser
    """
    df = pd.read_csv(unified_csv_file)
    data_list = []

    # itération sur chaque ligne pour normalisation
    for row in df.itertuples():
        data_list.append({
                "nom": row.nom,
                "date": row.date,
                "latitude": round(row.latitude, 4), # Précision à 4 décimales ≈ 11m
                "longitude": round(row.longitude, 4)
            })
        
    # Stockage dans un dataframe & enregistrement au format CSV
    new_df = pd.DataFrame(data_list)
    new_df.to_csv(unified_csv_file, encoding="utf-8")  # On écrase la version du CSV non-normalisée



### Fonction principale ###

def main_03(input_folder, output_folder):
    unified_csv_file = multiple_to_one_csv(input_folder, output_folder)
    dataframe_normalizer(unified_csv_file)
    file_name = os.path.basename(unified_csv_file)
    print(f"\nL'ensemble des fichiers CSV ont été fusionnés en un unique fichier normalisé, nommé '{file_name}'.")
    return unified_csv_file