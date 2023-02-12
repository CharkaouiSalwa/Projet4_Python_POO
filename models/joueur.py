import uuid
class Joueur:
    """
    Création de la class Joueur avec l'initialisation des attributs
    """
    def __init__(self,id_national, nom, prenom, date_naissance):
        # generate unique id
        id_joueur = uuid.uuid4().int & (1 << 10) - 1
        self.id_joueur = id_joueur
        self.id_national = id_national
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance

    def __str__(self):
        return self.id_national + " " + self.nom + " " + self.prenom + " né(e) le " + str(self.date_naissance)

    def __repr__(self):
        return self.id_national + " " + self.nom + " " + self.prenom + " né(e) le " + str(self.date_naissance)

