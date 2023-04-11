from controllers.tourController import Tourcontroller
import views.menuView


class TourView:
    def ajouter_tour(self):
        try:
            while views.menuView.nomTournoi and len(str(views.menuView.nomTournoi)) < 3:
                try:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                    if len(str(views.menuView.nomTournoi)) < 3:
                        print("Le nom du tournoi doit contenir au minimum trois caractères.")
                except Exception:
                    print("Le nom du tournoi n'est pas valide.")
                    views.menuView.nomTournoi = ""

            while type(views.menuView.nomTour) != str or len(str(views.menuView.nomTour)) < 3:
                try:
                    views.menuView.nomTour = str(input("Veuillez saisir le nom du tour : "))
                    if len(str(views.menuView.nomTour)) < 3:
                        print("Le nom du tour doit contenir au minimum trois caractères.")
                        views.menuView.nomTour = ""
                except Exception:
                    print("Le nom du tour n'est pas valide.")
                    views.menuView.nomTour = ""
            v = Tourcontroller.add_tour(self, views.menuView.nomTournoi, views.menuView.nomTour)
            print(v)
        except Exception as e:
            views.menuView.nomTournoi = ""
            print("Erreur : ", e)

    def afficher_tours_du_tournoi(self):
        """afficher tous les tours d'un tournoi"""
        while True:
            try:
                while not views.menuView.nomTournoi:
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
                                print("\t\tJoueur 1 : " + match["id_national_1"] + " son score : "
                                      + str(match["score_J1"])
                                      + " CONTRE " + "Joueur 2 : " + match["id_national_2"] + " son score : " + str(
                                    match["score_J2"]))
                        print("\n")
                    break
                else:
                    views.menuView.nomTournoi = ""
                    word = "No such file or directory"
                    if word in str(tours):
                        print("Ce tournoi n'existe pas.")
                    else:
                        print(tours)
            except Exception as e:
                views.menuView.nomTournoi = ""
                print("Erreur : ", e)

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
