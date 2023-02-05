from controllers.tournoiController import tournoiController
from models.tournoi import Tournoi

class tournoiView:
    def ajoutertournoi(self):
        id_tournoi = input("Entrer l'id  : ")
        nom = input("Entrer le nom : ")
        lieu = input("Entrer le lieu : ")
        date_debut = input("Entrer la date de debut : ")
        date_fin = input("Entrer la date de fin : ")
        description = input("entrer la remarque :")
        nbr_tour = input("entrer le nombre de tour :")
        tour_actuel = input("entrer le tour actuel :")

        v = tournoiController.ajouter_tournoi(self,id_tournoi,nom,lieu,date_debut,date_fin,description,nbr_tour,tour_actuel)
        #v = tournoiController.ajouter_tournoi(self,1,'test','test','test','test','test')
        print(v)

