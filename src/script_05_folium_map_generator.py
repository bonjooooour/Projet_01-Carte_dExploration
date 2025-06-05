"""
Fichier : script_05_folium_exploration_map.py

Génère un carte du monde grâce à la librairie Folium, afin d'afficher les lieux visités sur l'ensemble du globe.
- Récolte les coordonnées GPS (latitude, longitude) de mes activités, stockées dans un fichier CSV, préalablement traité.
- Génère une carte à l'aide de la librairie Folium et les fonds de carte Stadia Maps.
- Génère des points de chaleur de chaleur ou 'heatmap' pour représenter les zones visitées, 
où l'intensité des couleurs varie en fonction de la densité des points.
- Ajout de fonctionnalités complémentaires : choix du thème de la carte, mini-carte d'angle.
- Enregistrement de la carte générée au sein d'un fichier HTML.
"""



### Librairies ###
import pandas as pd
import folium
from folium.plugins import HeatMap
from folium.plugins import MiniMap
from datetime import datetime



### Nom du fichier de sortie ###
FOLIUM_MAP_NAME = 'MY_EXPLORATION_MAP__final_version_'+str(datetime.now().date())+'.html'



### Clé API Stadia Maps (pour fonds de carte) ###
STADIA_API_KEY = 'c1bc49f0-96a3-4360-a30f-3b5fc9a4dc41'


### Fonction unique ###

def main_05(csv_file_to_display, output_folder):
    """
    param : 
    - csv_file_to_display : fichier CSV contenant les données de posisitons, préalablement traitées
    - output_folder : chemin d'accès pour l'emplacement de sauvegarde

    sortie :
    - MY_EXPLORATION_MAP__final_version_YYYY-MM-DD : carte du monde avec les zones que j'ai pu visiter à la date indiquée, au format HTML
    """
    
    # 1 # Collecte des données
                                                       
    df = pd.read_csv(csv_file_to_display)      # Dataframe
    list_GPS = []                   # Liste vide stockant les couples [latitude, longitude]
    
    # Itération des lignes du dataframe et collecte des données de localisation
    for row in df.itertuples():
        latitude = row.latitude
        longitude = row.longitude
        list_GPS.append([latitude, longitude])


    # 2 # Création de la carte Folium

    # Initialisation de la carte
    map = folium.Map(
        location=(48.8622893, 2.3526954),   # Position d'affichage par défaut
        tiles=None,
        zoom_start = 7                      # zoom par défaut
    )

    # Liste des différents fonds de carte Stadia
    MAPS_TILES = [
        'alidade_smooth_dark', 
        'alidade_satellite',
        'alidade_smooth',  
        'alidade_bright'
    ]

    # Choix du fond de carte
    MAP_1 = str(MAPS_TILES[0])   
    MAP_2 = str(MAPS_TILES[1])        

    # Vue satellite
    folium.TileLayer(
        tiles=f'https://tiles.stadiamaps.com/tiles/{MAP_2}/{{z}}/{{x}}/{{y}}{{r}}.png?api_key={STADIA_API_KEY}',
        attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a>, &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        name='Vue satellite',
        control=True
    ).add_to(map)

    # Thème sombre
    folium.TileLayer(
        tiles=f'https://tiles.stadiamaps.com/tiles/{MAP_1}/{{z}}/{{x}}/{{y}}{{r}}.png?api_key={STADIA_API_KEY}',
        attr='&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a>, &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
        name='Thème sombre',
        control=True
    ).add_to(map)


    # 3 # Affichage des données sur la carte
    
    # Création d'une 'HeatMap' à partir des coordonnées récoltées et ajout sur la carte
    HeatMap(list_GPS,               # Valeurs de réf :
        min_opacity=.6,             # .6
        max_opacity=.6,             # .6
        radius=12,                  # 11
        blur=20,                    # 19
        gradient={.2: "#edafab", .4: "#bad3e8", .9: "#e8ceb7"}, # Dégradé de couleurs
        name='Zone explorée'
    ).add_to(map)


    # 4 # Fonctionnalités supplémentaires

    # Plein écran
    folium.plugins.Fullscreen(
        position="topright",
        title="Plein écran",
        title_cancel="Réduire",
        force_separate_button=True,
    ).add_to(map)

    # Mini carte d'angle
    MiniMap().add_to(map)

    # Sélection fond de carte
    folium.LayerControl().add_to(map)


    # 5 # Affichage final et sauvegarde de la carte dans un fichier .html
    map
    map.save(output_folder+"/"+FOLIUM_MAP_NAME)
    print(f"\nMa carte d'exploration du monde à date du {datetime.now().date()} a été générée avec succès. ✅\n\nBonne balade ! 🧭")