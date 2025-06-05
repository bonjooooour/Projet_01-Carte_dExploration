"""
Fichier : script_04_data_reduction_algorithm.py

Réduit la quantité de données GPS présente dans le fichier CSV unifier.
- Définition arbitraire d'un seuil de proximité, Lambda, à partir du quel 2 points sont coinsidérés comme "très proches voisins".
- Passe en revue chaque couple de coordonnées (latitude, longitude) 
et supprime du dataframe les couples voisins ayant une distance euclidienne "très proche" du couple de référence.
"""



### Librairies ###
import pandas as pd
from datetime import datetime
from scipy.spatial import cKDTree



### Nom du fichier de sortie et constante ###

# nom de sortie du fichier CSV final
FINAL_REDUCED_CSV_FILE_NAME = "FINAL_REDUCED_DATAFRAME_"+str(datetime.now().date())+".csv"

# Seuil de proximité entre points (lat, long) voisins, défini arbitrairement
LAMBDA = 0.00035      # ≈ 11m     (distance euclidienne entre 2 pts)



### Fonction unique : algorithme de réduction de données ###

def main_04(large_unified_csv_file, output_folder):
    """ 
    param:
    - large_unified_csv_file : fichier CSV normalisé conetnant un grand nombre de données 
    - output_folder : dossier de sortie

    sortie :
    - reduced_unified_csv_file : fichier CSV final, normalisé, réduit en nombre de données
    """
    # Seuil de proximité entre points (lat, long) voisins, défini arbitrairement
    Lambda = LAMBDA

    # Création du dataframe
    df = pd.read_csv(large_unified_csv_file)                    # Lecture du fichier CSV à réduire
    df = df.drop(columns='Unnamed: 0', errors='ignore')         # suppresion d'une colonne inutile
    
    # Suppression des lignes contenant des NaN
    df = df.dropna(subset=['latitude', 'longitude'])
    df = df.reset_index(drop=True)
    N = len(df)

    # Extraction des coordonnées GPS et convertion du df en un tableau NumPy 2D (N, 2)
    coords = df[['latitude', 'longitude']].values   

    # Création d'un arbre 2-dimensionnel cKDTree, pour recherche spatiale
    tree = cKDTree(coords)

    # Initialisation de l'ensemble contenant les points à supprimer
    coords_to_delete = set()

    # Itération de l'ensemble des points de coords
    for i in range(N):
        # Si le pt est déjà marqué comme à supprimer, on passe
        if i in coords_to_delete:
            continue 
        
        # Recherche des proches voisins présent sous le seuil Lambda
        neighbors = tree.query_ball_point(coords[i], Lambda)    # Calcul de la distance euclidienne intégré
        neighbors = [n for n in neighbors if n != i]            # Exclusion du couple de coords d'indice i (car distance entre un point et lui même forcément = 0 donc < Lambda)
        coords_to_delete.update(neighbors)                      # Ajout des proches voisins dans l'ensemble des points à suppr 

    # Suppression finale de l'ensemble des coordonnées définies comme "proches voisins" d'un autre couple
    df_reduced = df.drop(index=coords_to_delete).reset_index(drop=True)
    print("Pour Lambda ≈ 11m")
    print(f"Lignes supprimées : {len(coords_to_delete)}")
    print(f"Lignes conservées : {len(df_reduced)}")
    print("\nRéduction de données terminée.\nFichier CSV final généré.")
    
    # Sauvegarde du fichier CSV final
    final_reduced_csv_file = output_folder + "/" + FINAL_REDUCED_CSV_FILE_NAME
    df_reduced.to_csv(final_reduced_csv_file, index=False, encoding="utf-8")
    return final_reduced_csv_file