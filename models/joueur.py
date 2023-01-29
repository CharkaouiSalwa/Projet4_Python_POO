
class Joueur:
    """

    """
    def __init__(self,id_national, nom, prenom, date_naissance):
        self.id_national = id_national
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def __str__(self):
        return self.id_national + " " + self.nom + " " + self.prenom + " né(e) le " + str(self.date_naissance)

    def __repr__(self):
        return self.id_national + " " + self.nom + " " + self.prenom + " né(e) le " + str(self.date_naissance)

