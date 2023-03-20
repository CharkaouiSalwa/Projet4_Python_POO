import uuid


class Tournoi:
    """ Création de la class Joueur avec l'initialisation des attributs"""
    def __init__(self, nom_tournoi, lieu, date_debut, remarque,
                 nbr_tour=4, tour_actuel=0, joueurs=[], tours=[]):
        id_tournoi = uuid.uuid4().int & (1 << 10) - 1
        self.id_tournoi = id_tournoi
        self.nom_tournoi = nom_tournoi
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = ""
        self.remarque = remarque
        self.nbr_tour = nbr_tour
        self.tour_actuel = tour_actuel
        self.joueurs = joueurs
        self.tours = tours
