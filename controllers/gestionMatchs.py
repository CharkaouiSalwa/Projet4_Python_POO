


def definir_gagnent(joueurs):
    # trouver le joueur avec le plus de points
    gagnat = None
    max_points = 0
    for joueur in joueurs:
        if joueur["points"] > max_points:
            max_points = joueur["points"]
            gagnat = joueur
    return gagnat

# exemple d'utilisation de la fonction
joueurs = [
    {"nom": "joueur1", "points": 10},
    {"nom": "joueur2", "points": 20},
    {"nom": "joueur3", "points": 15}
]
gagnat = definir_gagnent(joueurs)
print(gagnat["nom"]) # affichier le joueur2