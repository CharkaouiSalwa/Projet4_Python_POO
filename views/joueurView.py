from models.joueur import Joueur
from controllers.joueurController import joueurController
from controllers.tournoiController import tournoiController


class JoueurView():
    def add_joueur(self,nom_tournoi):


        #id_national input validation
        id_national = ""
        while len(str(id_national)) < 3 and len(str(id_national)) > 6 :
            try:
                id_national = str(input("Veuillez saisir l'id national : "))
                if len(str(id_national)) < 3 and len(str(id_national)) > 6:
                    print("L'id national doit contenir au minimum trois caractères et doit pas dépasser 6 caractères.")
            except Exception as e :
                print("L'id national n'est pas valide'.")
                id_national = ""

        #nom input validation
        nom = ""
        while len(str(nom)) < 3:
            try:
                nom = str(input("Veuillez saisir le nom du joueur : "))
                if len(str(nom)) < 3:
                    print("Le nom du joueur doit contenir au minimum trois caractères.")
            except Exception as e :
                print("Le nom du joueur n'est pas valide.")
                nom = ""
        # prenom input validation
        prenom = ""
        while len(str(prenom)) < 3:
            try:
                prenom = str(input("Veuillez saisir le prenom du joueur : "))
                if len(str(prenom)) < 3:
                    print("Le prenom du joueur doit contenir au minimum trois caractères.")
            except Exception as e :
                print("Le prenom du joueur n'est pas valide.")
                prenom = ""

        # date_naissance input validation
        date_naissance = ""
        while len(str(date_naissance)) != 10:
            try:
                date_naissance = str(input("Veuillez saisir la date de naissance du joueur : "))
                if len(str(date_naissance)) != 10 and tournoiController.validate(date_naissance) == False:
                    print("La date de naissance du joueur doit avoir le format jj/mm/aaaa.")
            except Exception as e :
                print("La date de naissance du joueur n'est pas valide.")
                date_naissance = ""

        v = joueurController.ajouter_joueur(self,nom_tournoi,id_national, nom, prenom, date_naissance )
        print(v)
