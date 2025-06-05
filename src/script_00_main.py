"""
Fichier : script_00_main.py

Description du projet :
L'objectif de ce projet est de collecter l'ensemble des données de positions accumulées au cours 
de mes activités sportives (courses à pied, balades à vélo) et photographiques, 
afin de répertorier et d'afficher sur une carte du monde, l'ensemble des lieux que j'ai, à date, pu visiter.
Les zones ainsi déjà explorées s'affichent sur la carte par des nuages de couleurs graduées, représentant l'intensité d'exploration des lieux.

Fonctionnement :
- Ce fichier fait le lien entre les 5 parties de ce projet. Il automatise l'ensemble du processus du projet. 
- L'utilisateur n'a qu'une tâche à effectuer manuellement : Importer dans le fichier "data/01_strava_RAW_files" 
l'archive de ses activités Strava, préalablement téléchargée depuis le site web.
- Ensuite, il ne reste plus qu'à lancer ce script, et la carte d'exploration sera générée et stockée dans le dossier 'data/04_final_FOLIUM_MAP'.
"""



### Importation des scripts externes ###
import script_01_apple_photos_data_scrap_to_csv as script_01
import script_02_strava_activities_data_to_csv as script_02
import script_03_multiple_to_one_csv as script_03
import script_04_data_reduction_algorithm as script_04
import script_05_folium_exploration_map as script_05



### Chemins d'accès ###

# Chemins d'entrée
SRTAVA_RAW_DATA_FOLDER = 'data/01_strava_RAW_files/activities'

# Chemins de sortie
CSV_FILES_FOLDER = 'data/02_intermediate_CSV_files'
FINAL_CSV_FILES_FOLDER = 'data/03_final_DATAFRAME_files'
FINAL_FOLIUM_MAP_FOLDER = 'data/04_final_FOLIUM_MAP'


# ### Script 01 ### 
# # Collecte depuis ma librairie Apple Photos les métadonnées de positions, 
# # puis les stockage dans un fichier CSV normalisé.
# script_01.main_01(CSV_FILES_FOLDER) 
# print('\nscript 01 : ✅\n\n')


# ### Script 02 ###
# # Conversion des données d'activités Strava en fichiers CSV normalisés.
# script_02.main_02(SRTAVA_RAW_DATA_FOLDER, CSV_FILES_FOLDER)
# print('\nscript 02 : ✅\n\n')


### Script 03 ###
# Fusionne les multiples fichiers CSV préalablement générés, pour n'en avoir plus qu'un unique, normalisé.
UNIFIED_CSV_FILE_to_REDUCED = script_03.main_03(CSV_FILES_FOLDER, FINAL_CSV_FILES_FOLDER)
print('\nscript 03 : ✅\n\n')


### Script 04 ###
# Réduit la quantité de données du fichier CSV final grâce à un algorithme de recherche de proches voisins
FINAL_REDUCED_CSV_FILE = script_04.main_04(UNIFIED_CSV_FILE_to_REDUCED, FINAL_CSV_FILES_FOLDER)
print('\nscript 04 : ✅\n\n')




### Script 05 ###
# Génère ma carte d'exploration du monde à partir du fichier CSV contenant les coordonnées GPS de mes activités (sport & photos)
script_05.main_05(FINAL_REDUCED_CSV_FILE, FINAL_FOLIUM_MAP_FOLDER)
print('\nscript 05 : ✅\n\n')
