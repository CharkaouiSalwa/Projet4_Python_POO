from controllers.matchController import MatchController
import views.menuView

class MatchView:
    """Afficher la liste des matchs d'un tour"""
    def afficher_matchs_by_tour(self):
        try:
            while len(str(views.menuView.nomTournoi)) < 3:
                try:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                    if len(str(views.menuView.nomTournoi)) < 3:
                        print("Le nom du tournoi doit contenir au minimum trois caractères.")
                except Exception:
                    print("Le nom du tournoi n'est pas valide.")
                    views.menuView.nomTournoi = ""

            while len(str(views.menuView.nomTour)) < 3:
                try:
                    views.menuView.nomTour = str(input("Veuillez saisir le nom du tour : "))
                    if len(str(views.menuView.nomTour)) < 3:
                        print("Le nom du tour doit contenir au minimum trois caractères.")
                except Exception:
                    print("Le nom du tour n'est pas valide.")
                    views.menuView.nomTour = ""
            matchs = MatchController.get_matchs_by_tour(self, views.menuView.nomTournoi, views.menuView.nomTour)
            if type(matchs) == list:
                print("La liste des matchs d'un tour : \n")
                for match in matchs:
                    print("\t\tJoueur 1 : " + match["id_national_1"] + " son score : " + str(match["score_J1"])
                          + " CONTRE " + "Joueur 2 : " + match["id_national_2"] + " son score : " + str(
                        match["score_J2"]))
            else:
                print(matchs)
        except Exception as e:
            print(e)
    print("\n")

    """Définir le gagnant"""
    def gagnant(self):
        try:
            while len(str(views.menuView.nomTournoi)) < 3:
                try:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                    if len(str(views.menuView.nomTournoi)) < 3:
                        print("Le nom du tournoi doit contenir au minimum trois caractères.")
                except Exception:
                    print("Le nom du tournoi n'est pas valide.")
                    views.menuView.nomTournoi = ""

            while len(str(views.menuView.nomTour)) < 3:
                try:
                    views.menuView.nomTour = str(input("Veuillez saisir le nom du tour : "))
                    if len(str(views.menuView.nomTour)) < 3:
                        print("Le nom du tour doit contenir au minimum trois caractères.")
                except Exception:
                    print("Le nom du tour n'est pas valide.")
                    views.menuView.nomTour = ""

            id_national1 = ""
            while len(str(id_national1)) != 6:
                try:
                    id_national1 = str(input("Veuillez saisir l'id national du premier joueur qui "
                                             "a joué dans ce match :"))
                    if len(str(id_national1)) != 6:
                        print("L'id national doit contenir au minimum trois caractères "
                              "et doit pas dépasser 6 caractères.")
                except Exception:
                    print("L'id national n'est pas valide'.")
                    id_national1 = ""

            id_national2 = ""
            while len(str(id_national2)) != 6:
                try:
                    id_national2 = str(input("Veuillez saisir l'id national du deuxième "
                                             "joueur qui a joué dans ce match :"))
                    if len(str(id_national2)) != 6:
                        print("L'id national doit contenir au minimum trois caractères "
                              "et doit pas dépasser 6 caractères.")
                except Exception:
                    print("L'id national n'est pas valide'.")
                    id_national2 = ""

            try:
                winner = str(
                    input("Veuillez saisir l'id national du joueur qui a gnagné dans ce match "
                          "(si le match est null, appuyer directement sur entrer): "))
            except Exception:
                print("L'id national n'est pas valide'.")
                winner = ""

            gagnant = MatchController.match_winner(self, views.menuView.nomTournoi, views.menuView.nomTour, id_national1, id_national2, winner)
            print(gagnant)
        except Exception as e:
            print(e)
    """Créer un match d'un tour"""
    def create_match(self):
        try:
            while len(str(views.menuView.nomTournoi)) < 3:
                try:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                    if len(str(views.menuView.nomTournoi)) < 3:
                        print("Le nom du tournoi doit contenir au minimum trois caractères.")
                except Exception:
                    print("Le nom du tournoi n'est pas valide.")
                    views.menuView.nomTournoi = ""

            while len(str(views.menuView.nomTour)) < 3:
                try:
                    views.menuView.nomTour = str(input("Veuillez saisir le nom du tour : "))
                    if len(str(views.menuView.nomTour)) < 3:
                        print("Le nom du tour doit contenir au minimum trois caractères.")
                except Exception:
                    print("Le nom du tour n'est pas valide.")
                    views.menuView.nomTour = ""

            m = MatchController.creer_matchs(self, views.menuView.nomTournoi, views.menuView.nomTour)
            print(m)
        except Exception as e:
            print(e)
