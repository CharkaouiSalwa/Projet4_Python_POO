import uuid


class Tournoi:
    def __init__(self, nom_tournoi, lieu, date_debut, date_fin, remarque,
                 nbr_tour=4, tour_actuel=0, joueurs=[], tours=[]):
        id_tournoi = uuid.uuid4().int & (1 << 10) - 1
        self.id_tournoi = id_tournoi
        self.nom_tournoi = nom_tournoi
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.remarque = remarque
        self.nbr_tour = nbr_tour
        self.tour_actuel = tour_actuel
        self.joueurs = joueurs
        self.tours = tours

    def __str__(self):
        print("Le tournoi N° ", self.id_tournoi, "son nom: ", self.nom_tournoi, "se pass au: ",
              self.lieu, "le : ", self.date_debut, "et se termine le :", self.date_fin, "ses remarques :",
              self.remarque, "nobmbre de tour :",
              self.nbr_tour, "la tour N :", self.tour_actuel)
