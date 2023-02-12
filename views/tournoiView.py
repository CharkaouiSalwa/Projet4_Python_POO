from controllers.tournoiController import tournoiController
from models.tournoi import Tournoi
import json

class tournoiView:
    def ajoutertournoi(self):
        #nom input validation
        nom = ""
        while len(str(nom)) < 3:
            try:
                nom = str(input("Veuillez saisir le nom du tournoi : "))
                if len(str(nom)) < 3:
                    print("Le nom du tournoi doit contenir au minimum trois caractères.")
            except Exception as e :
                print("Le nom du tournoi n'est pas valide.")
                nom = ""

        # lieu input validation
        lieu = ""
        while len(str(lieu)) < 3:
            try:
                lieu = str(input("Veuillez saisir le lieu du tournoi : "))
                if len(str(lieu)) < 3:
                    print("Le lieu du tournoi doit contenir au minimum trois caractères.")
            except Exception as e :
                print("Le lieu du tournoi n'est pas valide.")
                lieu = ""

        # date_debut input validation
        date_debut = ""
        while len(str(date_debut)) != 10:
            try:
                date_debut = str(input("Veuillez saisir la date de debut du tournoi : "))
                if len(str(date_debut)) != 10 and tournoiController.validate(date_debut) == False:
                    print("La date de debut du tournoi doit avoir le format jj/mm/aaaa.")
            except Exception as e :
                print("La date de debut du tournoi n'est pas valide.")
                date_debut = ""

        # date_fin input validation
        date_fin = ""
        while len(str(date_fin)) != 10 or tournoiController.validate(date_fin) == False or date_fin < date_debut:
            try:
                date_fin = str(input("Veuillez saisir la date de fin du tournoi : "))
                if len(str(date_fin)) != 10 and tournoiController.validate(date_fin) == False:
                    print("La date de fin du tournoi doit avoir le format jj/mm/aaaa.")
                elif date_fin < date_debut:
                    print('La date de fin du tournoi doit etre superieur ou égal à la date de debut.')
            except Exception as e :
                print("La date de fin du tournoi n'est pas valide.")
                date_fin = ""

        # remarque input validation
        remarque = ""
        while len(str(remarque)) < 3:
            try:
                remarque = str(input("Veuillez saisir la remarque : "))
                if len(str(remarque)) < 3:
                    print("la remarque du tournoi doit contenir au minimum trois caractères.")
            except Exception as e :
                print("la remarque du tournoi n'est pas valide.")
                lieu = ""



        v = tournoiController.add_tournoi(self,nom,lieu,date_debut,date_fin,remarque)
        print(v)

    """
    afficher tous les tournois qui existe dans plusieurs fichier json
    """







"""
afficher le nom et la date d'une tournoi
"""









