from models.tour import Tour

class Tournoi:
    def __init__(self,id_tournoi , nom, lieu, date_debut,
                 date_fin ,description, nbr_tour = 4 ,tour_actuel = 0):
        self.id_tournoi = id_tournoi
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.description = description
        self.nbr_tour = nbr_tour
        self.tour_actuel = tour_actuel


    def __str__(self):
        print("Le tournoi N° ", self.id_tournoi, "son nom: ", self.nom,  "se pass au: ",
              self.lieu, "le : ",self.date_debut, "et se termine le :", self.date_fin, "ses remarques :", self.description, "nobmbre de tour :",
              self.nbr_tour,"la tour N :", self.tour_actuel)