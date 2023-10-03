import math 
# Demande à l'utilisateur de saisir la longueur et la largeur du bâtiment
longueur = float(input("Entrez la longueur du bâtiment en mètres : "))
largeur = float(input("Entrez la largeur du bâtiment en mètres : "))

# Calcule la surface du bâtiment en multipliant la longueur par la largeur
surface = longueur * largeur

# Calcule le périmètre du bâtiment
perimetre = 2 * (longueur + largeur)

# Longueur d'une planche de bois
longueur_bois = 4

# Calcule le nombre de planches de bois nécessaires
nombre_de_bois = perimetre / longueur_bois

# Affiche la surface du bâtiment
print("La surface du bâtiment est de", surface, "mètres carrés.")

# Affiche la quantité de bois nécessaire
print("La quantité de bois nécessaire est de", nombre_de_bois, "planches de 4 mètres chacune.")
