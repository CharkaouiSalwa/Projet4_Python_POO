from controllers.matchController import MatchController
import views.menuView


class MatchView:
    def afficher_matchs_by_tour(self):
        """Afficher la liste des matchs d'un tour"""
        try:
            while len(str(views.menuView.nomTournoi)) < 3:
                try:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                    if len(str(views.menuView.nomTournoi)) < 3:
                        print("Le nom du tournoi doit contenir au minimum trois caractères.")
                        views.menuView.nomTournoi = ""
                except Exception:
                    print("Le nom du tournoi n'est pas valide.")
                    views.menuView.nomTournoi = ""

            while len(str(views.menuView.nomTour)) < 3:
                try:
                    views.menuView.nomTour = str(input("Veuillez saisir le nom du tour : "))
                    if len(str(views.menuView.nomTour)) < 3:
                        print("Le nom du tour doit contenir au minimum trois caractères.")
                        views.menuView.nomTour = ""
                except Exception:
                    print("Le nom du tour n'est pas valide.")
                    views.menuView.nomTour = ""
            matchs = MatchController.get_matchs_by_tour(self, views.menuView.nomTournoi, views.menuView.nomTour)
            if type(matchs) == list:
                print("La liste des matchs du tour : \n")
                i = 1
                for match in matchs:
                    print("\t\tMatch " + str(i)+" - Joueur 1 : " + match["id_national_1"] +
                          " son score : " + str(match["score_J1"])
                          + " CONTRE " + "Joueur 2 : " + match["id_national_2"] + " son score : " + str(
                        match["score_J2"]))
                    i += 1
            else:
                views.menuView.nomTour = ""
                word = "No such file or directory"
                if word in str(matchs):
                    print("Ce tournoi n'existe pas.")
                    views.menuView.nomTournoi = ""
                else:
                    print(matchs)
        except Exception as e:
            views.menuView.nomTour = ""
            print("Erreur : ", e)
        print("\n")

    def gagnant(self):
        """Définir le gagnant"""
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

            while len(str(views.menuView.joueur1)) != 6:
                try:
                    views.menuView.joueur1 = str(input("Veuillez saisir l'id national du premier joueur "
                                                       "qui a joué dans ce match :"))
                    if len(str(views.menuView.joueur1)) != 6:
                        print("L'id national doit contenir au minimum trois caractères "
                              "et doit pas dépasser 6 caractères.")
                except Exception:
                    print("L'id national n'est pas valide'.")
                    views.menuView.joueur1 = ""

            while len(str(views.menuView.joueur2)) != 6:
                try:
                    views.menuView.joueur2 = str(input("Veuillez saisir l'id national du deuxième "
                                                       "joueur qui a joué dans ce match :"))
                    if len(str(views.menuView.joueur2)) != 6:
                        print("L'id national doit contenir au minimum trois caractères "
                              "et doit pas dépasser 6 caractères.")
                except Exception:
                    print("L'id national n'est pas valide'.")
                    views.menuView.joueur2 = ""

            winner = ""
            while (winner == ""):
                try:
                    winner = str(input("Veuillez saisir l'id national du joueur gagnant "
                                       "(si le match est null, appuyer directement sur entrer): "))
                    if winner != views.menuView.joueur1 and winner != views.menuView.joueur2 and winner != '':
                        print("L'id national n'est pas valide'.")
                        winner = ""
                    else:
                        break
                except Exception:
                    print("L'id national n'est pas valide'.")
                    winner = ""

            gagnant = MatchController.match_winner(self, views.menuView.nomTournoi, views.menuView.nomTour,
                                                   views.menuView.joueur1, views.menuView.joueur2, winner)
            print(gagnant)
        except Exception as e:
            print(e)

    def create_match(self):
        """Créer un match d'un tour"""
        try:
            while len(str(views.menuView.nomTournoi)) < 3:
                try:
                    views.menuView.nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                    if len(str(views.menuView.nomTournoi)) < 3:
                        print("Le nom du tournoi doit contenir au minimum trois caractères.")
                        views.menuView.nomTournoi = ""
                except Exception:
                    print("Le nom du tournoi n'est pas valide.")
                    views.menuView.nomTournoi = ""

            while len(str(views.menuView.nomTour)) < 3:
                try:
                    views.menuView.nomTour = str(input("Veuillez saisir le nom du tour : "))
                    if len(str(views.menuView.nomTour)) < 3:
                        print("Le nom du tour doit contenir au minimum trois caractères.")
                        views.menuView.nomTour = ""
                except Exception:
                    print("Le nom du tour n'est pas valide.")
                    views.menuView.nomTour = ""

            m = MatchController.creer_matchs(self, views.menuView.nomTournoi, views.menuView.nomTour)
            print(m)
        except Exception as e:
            print(e)
