from controllers.tourController import Tourcontroller
import views.menuView


class TourView:
    def ajouter_tour(self):
        try:
            views.menuView.nomTour = ""
            if not views.menuView.nomTournoi:
                views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
            views.menuView.nomTour = str(input("Veuillez saisir le nom du tour : "))
            v = Tourcontroller.add_tour(self, views.menuView.nomTournoi, views.menuView.nomTour)
            print(v)
        except Exception as e:
            return e

    """afficher tous les tours d'un tournoi"""

    def afficher_tours_du_tournoi(self):
        try:
            if not views.menuView.nomTournoi:
                views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
            tours = Tourcontroller.get_tours_by_tournoi(self, views.menuView.nomTournoi)
            if type(tours) == list:
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
            else:
                print(tours)

        except Exception as e:
            return e

    def fermer_tour(self):
        try:
            if not views.menuView.nomTournoi:
                views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
            if not views.menuView.nomTour:
                views.menuView.nomTour = str(input("Veuillez saisir le nom du tour : "))
            v = Tourcontroller.close_tour(self, views.menuView.nomTournoi, views.menuView.nomTour)
            print(v)
        except Exception as e:
            return e
