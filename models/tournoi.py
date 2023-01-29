from models.tour import Tour

class Tournoi:
    def __init__(self,id , nom, lieu, date_debut,
                 date_fin ,description, tour_actuel = 0 ,nbr_tour = 4):
        self.id = id
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nbr_tour = nbr_tour
        self.tour_actuel = tour_actuel
        self.description = description