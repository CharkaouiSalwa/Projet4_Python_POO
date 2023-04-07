from controllers.joueurController import JoueurController
from controllers.tournoiController import TournoiController
import views.menuView
PATH = "data/tournaments/"


class JoueurView:
    def add_joueur(self):
        try:
            boolok = False
            while not boolok:
                while len(str(views.menuView.nomTournoi)) < 3:
                    try:
                        views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                        if len(str(views.menuView.nomTournoi)) < 3:
                            print("Le nom du tournoi doit contenir au minimum trois caractères.")
                            views.menuView.nomTournoi = ""
                    except Exception:
                        print("Le nom du tournoi n'est pas valide.")
                        views.menuView.nomTournoi = ""

                id_national = ""
                while len(str(id_national)) != 6:
                    try:
                        id_national = str(input("Veuillez saisir l'id national : "))
                        if len(str(id_national)) != 6:
                            print("L'id national doit contenir 2 lettres et 4 chiffres (ex: AB1234).")
                            id_national = ""
                    except Exception:
                        print("L'id national n'est pas valide'.")
                        id_national = ""

                nom = ""
                while len(str(nom)) < 3:
                    try:
                        nom = str(input("Veuillez saisir le nom du joueur : "))
                        if len(str(nom)) < 3:
                            print("Le nom du joueur doit contenir au minimum trois caractères.")
                            nom = ""
                    except Exception:
                        print("Le nom du joueur n'est pas valide.")
                        nom = ""
                # prenom input validation
                prenom = ""
                while len(str(prenom)) < 3:
                    try:
                        prenom = str(input("Veuillez saisir le prenom du joueur : "))
                        if len(str(prenom)) < 3:
                            print("Le prenom du joueur doit contenir au minimum trois caractères.")
                            prenom = ""
                    except Exception:
                        print("Le prenom du joueur n'est pas valide.")
                        prenom = ""
                # date_naissance input validation
                date_naissance = ""
                while len(str(date_naissance)) != 10:
                    try:
                        date_naissance = str(input("Veuillez saisir la date de naissance du joueur : "))
                        if len(str(date_naissance)) != 10 or not TournoiController.validate(date_naissance):
                            print("La date de naissance du joueur doit avoir le format jj/mm/aaaa.")
                            date_naissance = ""
                    except Exception:
                        print("La date de naissance du joueur n'est pas valide.")
                        date_naissance = ""
                v = JoueurController.add_joueur(self, views.menuView.nomTournoi, id_national,
                                                nom, prenom, date_naissance)
                if v == 'Le joueur a été ajouté avec succès':
                    boolok = True
                    print(v)
                else:
                    print(v)
        except Exception as e:
            print(e)
    """afficher tous les joueurs de tous les tournois"""
    def afficher_joueurs(self):
        try:
            joueurs = JoueurController.get_all_joueurs(self, PATH)
            if type(joueurs) == list:
                print("\tLa liste des joueurs :\n")
                for joueur in joueurs:
                    print("\tID National : ", joueur["id_national"])
                    print("\tNom : ", joueur["nom"])
                    print("\tPrénom : ", joueur["prenom"])
                    print("\tDate de naissance : ", joueur["date_naissance"])
                    print("\n")
                    print("-----------------------------------------------\n")
            else:
                print(joueurs)
        except Exception as e:
            return e
    """ retourner tous les joueurs d'un tournoi """
    def afficher_joueurs_tournoi(self):
        while True:
            try:
                while not views.menuView.nomTournoi:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                joueurs = JoueurController.get_joueurs_by_tournoi(self, views.menuView.nomTournoi)
                if type(joueurs) == list:
                    print("\tLa liste des joueurs :\n")
                    for joueur in joueurs:
                        print("\tID National : ", joueur["id_national"])
                        print("\tNom : ", joueur["nom"])
                        print("\tPrénom : ", joueur["prenom"])
                        print("\tDate de naissance : ", joueur["date_naissance"])
                        print("\n")
                        print("-----------------------------------------------\n")
                    break
                else:
                    views.menuView.nomTournoi = ""
                    word = "No such file or directory"
                    if word in str(joueurs):
                        print("Ce tournoi n'existe pas.")
                    else:
                        print(joueurs)
            except Exception as e:
                views.menuView.nomTournoi = ""
                print("Erreur : ", e)
