from controllers.tourController import tourcontroller
import json


class tourView:
    def ajouter_tour(self):
        try:
            nom_tour = str(input("Veuillez saisir le nom du tour : "))
            nom_tournoi = str(input("Veuillez saisir le nom du tournoi : "))
            v = tourcontroller.add_tour(self, nom_tournoi, nom_tour)
            print(v)
        except Exception as e:
            return e

    """
    afficher tous les tours d'un tournoi
    """

    def afficher_tours_du_tournoi(self):
        try:
            nom_tournoi = str(input("Veuillez saisir le nom du tournoi : "))
            v = tourcontroller.get_tours_by_tournoi(self, nom_tournoi)
            v = json.dumps(v, indent=4)
            print("la liste des tours par tournoi", v)
        except Exception as e:
            return e

    def fermer_tour(self):
        try:
            nom_tour = str(input("Veuillez saisir le nom du tour : "))
            nom_tournoi = str(input("Veuillez saisir le nom du tournoi : "))
            v = tourcontroller.close_tour(self, nom_tournoi, nom_tour)
            print(v)
        except Exception as e:
            return e
