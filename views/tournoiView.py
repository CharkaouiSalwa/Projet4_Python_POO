from controllers.tournoiController import TournoiController
import views.menuView

PATH = "data/tournaments/"


class TournoiView:
    def ajoutertournoi(self):
        try:
            views.menuView.nomTournoi = ""
            while len(str(views.menuView.nomTournoi)) < 3:
                try:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                    if len(str(views.menuView.nomTournoi)) < 3:
                        print("Le nom du tournoi doit contenir au minimum trois caractères.")
                except Exception:
                    print("Le nom du tournoi n'est pas valide.")
                    views.menuView.nomTournoi = ""

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
                    if len(str(date_debut)) != 10 or not TournoiController.validate(date_debut):
                        print("La date de debut du tournoi doit avoir le format jj/mm/aaaa.")
                        date_debut = ""
                except Exception:
                    print("La date de debut du tournoi n'est pas valide.")
                    date_debut = ""

            remarque = ""
            while len(str(remarque)) < 3:
                try:
                    remarque = str(input("Veuillez saisir la remarque : "))
                    if len(str(remarque)) < 3:
                        print("la remarque du tournoi doit contenir au minimum trois caractères.")
                except Exception:
                    print("la remarque du tournoi n'est pas valide.")
                    remarque = ""
            nbr_tour = 0
            while int(nbr_tour) < 1:
                try:
                    nbr_tour = int(input("Combien de tour voulez-vous ajouter ?"))
                except Exception:
                    print("Le nombre de tour n'est pas valide.")
                    nbr_tour = 0
            v = TournoiController.add_tournoi(self, views.menuView.nomTournoi, lieu, date_debut, remarque, nbr_tour)
            return v
        except Exception as e:
            return e

    def afficher_tournois(self):
        """afficher tous les tournois qui existe dans plusieurs fichier json"""
        try:
            v = TournoiController.get_tournois(self, PATH)
            if type(v) == list:
                print("La liste des tournois :\n")
                for tournoi in v:
                    print("Nom du tournoi : ", tournoi["nom_tournoi"])
                    print("Lieu du tournoi : ", tournoi["lieu"])
                    print("date de début du tournoi : ", tournoi["date_debut"])
                    if tournoi["date_fin"]:
                        print("date de fin du tournoi : ", tournoi["date_fin"])
                    print("Remarque : ", tournoi["remarque"])
                    print("Nombre de tours : ", tournoi["nbr_tour"])
                    print("Tour Actuel : ", tournoi["tour_actuel"])
                    if tournoi["joueurs"]:
                        joueurs = tournoi["joueurs"]
                        print("\n")
                        print("\tLa liste des joueurs :\n")
                        for joueur in joueurs:
                            print("\tID National : ", joueur["id_national"])
                            print("\tNom : ", joueur["nom"])
                            print("\tPrénom : ", joueur["prenom"])
                            print("\tDate de naissance : ", joueur["date_naissance"])
                            print("\n")
                    if tournoi["tours"]:
                        tours = tournoi["tours"]
                        print("\tLa liste des tours :\n")
                        for tour in tours:
                            print("\tNom du tour : ", tour["nom_tour"])
                            print("\tDate heure début du tour : ", tour["date_heure_debut"])
                            if tour["date_heure_fin"]:
                                print("\tDate heure fin du tour : ", tour["date_heure_fin"])
                            if tour["matchs"]:
                                print("\n")
                                print("\t\tLa liste des matchs :\n")
                                matchs = tour["matchs"]
                                for match in matchs:
                                    print("\t\tJoueur 1 : " + match["id_national_1"] + " son score : "
                                          + str(match["score_J1"]) + " CONTRE " + "Joueur 2 : "
                                          + match["id_national_2"] + " son score : " + str(match["score_J2"]))
                            print("\n")
                    print("-----------------------------------------------\n")
            else:
                print(v)

        except Exception as e:
            return e

    def afficher_nom_date_tournoi(self):
        """afficher le nom et la date d'une tournoi"""
        while True:
            try:
                while not views.menuView.nomTournoi:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                v = TournoiController.get_nom_date_tournoi(self, views.menuView.nomTournoi)
                if type(v) == list:
                    print("le nom du tournoi : ", v[0])
                    print("la date de debut du tournoi : ", v[1])
                    print("la date de fin du tournoi : ", v[2])
                    break
                else:
                    views.menuView.nomTournoi = ""
                    word = "No such file or directory"
                    if word in str(v):
                        print("Ce tournoi n'existe pas.")
                    else:
                        print(v)
            except Exception as e:
                views.menuView.nomTournoi = ""
                print("Erreur : ", e)
