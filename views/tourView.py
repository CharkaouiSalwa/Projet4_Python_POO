from controllers.tourController import tourcontroller


class tourView:
    def ajouter_tour(self):
        try:
            nom_tournoi = str(input("Veuillez saisir le nom du tournoi : "))
            nom_tour = str(input("Veuillez saisir le nom du tour : "))
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
            tours = tourcontroller.get_tours_by_tournoi(self, nom_tournoi)
            print("La liste des tours par tournoi: \n")
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
                        print("\t\tJoueur 1 : " + match["id_national_1"] + " son score : " + str(match["score_J1"])
                              + " CONTRE " + "Joueur 2 : " + match["id_national_2"] + " son score : " + str(
                            match["score_J2"]))
                print("\n")

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
