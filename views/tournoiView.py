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

        remarque = ""
        while len(str(remarque)) < 3:
            try:
                remarque = str(input("Veuillez saisir la remarque : "))
                if len(str(remarque)) < 3:
                    print("la remarque du tournoi doit contenir au minimum trois caractères.")
            except Exception:
                print("la remarque du tournoi n'est pas valide.")
                lieu = ""
        v = tournoiController.add_tournoi(self, nom, lieu, date_debut, remarque)
        print(v)

    """
    afficher tous les tournois qui existe dans plusieurs fichier json
    """
    def afficher_tournois(self):
        try:
            v = tournoiController.get_tournois(self, PATH)
            print("La liste des tournois :\n")
            for tournoi in v:
                print("Nom du tournoi : ",tournoi["nom_tournoi"])
                print("Lieu du tournoi : ",tournoi["lieu"])
                print("date de début du tournoi : ",tournoi["date_debut"])
                if tournoi["date_fin"]:
                    print("date de fin du tournoi : ",tournoi["date_fin"])
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
                        print("\tDate heure début du tour : ", tour["date_heure_debut_tour"])
                        if tour["date_heure_fin_tour"]:
                            print("\tDate heure fin du tour : ", tour["date_heure_fin_tour"])
                        if tour["matchs"]:
                            print("\n")
                            print("\t\tLa liste des matchs :\n")
                            matchs = tour["matchs"]
                            for match in matchs:
                                print("\t\tJoueur 1 : " + match["id_national_1"] + " son score : " + str(match["score_J1"])
                                      + " CONTRE " + "Joueur 2 : " + match["id_national_2"] + " son score : " + str(match["score_J2"]))
                        print("\n")
                print("-----------------------------------------------\n")

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
