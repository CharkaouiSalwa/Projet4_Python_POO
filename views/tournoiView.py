from controllers.tournoiController import tournoiController
import json
PATH = "data/tournaments/"


class tournoiView:
    def ajoutertournoi(self):
        nom = ""
        while len(str(nom)) < 3:
            try:
                nom = str(input("Veuillez saisir le nom du tournoi : "))
                if len(str(nom)) < 3:
                    print("Le nom du tournoi doit contenir au minimum trois caractères.")
            except Exception:
                print("Le nom du tournoi n'est pas valide.")
                nom = ""

        lieu = ""
        while len(str(lieu)) < 3:
            try:
                lieu = str(input("Veuillez saisir le lieu du tournoi : "))
                if len(str(lieu)) < 3:
                    print("Le lieu du tournoi doit contenir au minimum trois caractères.")
            except Exception:
                print("Le lieu du tournoi n'est pas valide.")
                lieu = ""

        date_debut = ""
        while len(str(date_debut)) != 10:
            try:
                date_debut = str(input("Veuillez saisir la date de debut du tournoi : "))
                if not len(str(date_debut)) != 10 and not tournoiController.validate(date_debut):
                    print("La date de debut du tournoi doit avoir le format jj/mm/aaaa.")
            except Exception:
                print("La date de debut du tournoi n'est pas valide.")
                date_debut = ""

        date_fin = ""
        while len(str(date_fin)) != 10 or not tournoiController.validate(date_fin) or date_fin < date_debut:
            try:
                date_fin = str(input("Veuillez saisir la date de fin du tournoi : "))
                if len(str(date_fin)) != 10 and not tournoiController.validate(date_fin):
                    print("La date de fin du tournoi doit avoir le format jj/mm/aaaa.")
                elif date_fin < date_debut:
                    print('La date de fin du tournoi doit etre superieur ou égal à la date de debut.')
            except Exception:
                print("La date de fin du tournoi n'est pas valide.")
                date_fin = ""

        remarque = ""
        while len(str(remarque)) < 3:
            try:
                remarque = str(input("Veuillez saisir la remarque : "))
                if len(str(remarque)) < 3:
                    print("la remarque du tournoi doit contenir au minimum trois caractères.")
            except Exception:
                print("la remarque du tournoi n'est pas valide.")
                lieu = ""
        v = tournoiController.add_tournoi(self, nom, lieu, date_debut, date_fin, remarque)
        print(v)

    """
    afficher tous les tournois qui existe dans plusieurs fichier json
    """
    def afficher_tournois(self):
        try:
            v = tournoiController.get_tournois(self, PATH)
            v = json.dumps(v, indent=4)
            print("la liste des tournois :", v)
        except Exception as e:
            return e
    """
    afficher le nom et la date d'une tournoi
    """
    def afficher_nom_date_tournoi(self):
        try:
            nom = str(input("Veuillez saisir le nom du tournoi : "))
            v = tournoiController.get_nom_date_tournoi(self, nom)
            print("le nom du tournoi : ", v[0])
            print("la date de debut du tournoi : ", v[1])
            print("la date de fin du tournoi : ", v[2])
        except Exception as e:
            return e
