class Match:
    """
    déclaration des attributs d'instance
    """
    def __init__(self, id_match, joueur_1, joueur_2, score):
        self.id_match = id_match
        self.joueur_1 = joueur_1
        self.joueur_2 = joueur_2
        self.score = score

    """
        retourner des tuples contient 
        les joueurs d'un tour et leurs score
    """
    def __str__(self):
        return "Le match :" + str(self.id_match) + "des joueurs" + str(self.joueur_1) + "Vs" + str(self.joueur_2)\
               + "leur score est :" + str(self.score)

    def __repr__(self):
        return "Le match :" + str(self.id_match) + "des joueurs" + str(self.joueur_1) + "Vs"+str(self.joueur_2)
        + "leur score est :" + str(self.score)