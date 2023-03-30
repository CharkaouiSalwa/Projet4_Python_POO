from controllers.menuController import gestion_tournois, gestion_tours,\
                                       gestion_joueurs, gestion_match
from controllers.matchController import MatchController
from controllers.tournoiController import TournoiController
from controllers.tourController import Tourcontroller
from controllers.menuController import MSG_EXIT
import os


def print_menu():

    print("1 -- Ajouter un nouveau tournoi")
    print("2 -- Continuer un tournoi")
    print("3 -- Afficher tous les tournois")
    print("4 -- Afficher tous les joueurs")
    print("5 -- Quitter")
def sous_menu():
    print("1 -- Afficher nom et date du tournois \t \t \t \t 2 -- Ajouter un tour ")
    print("3 -- Fermer un tour \t \t \t \t \t \t \t \t 4 -- Afficher les tours du tournois")
    print("5 -- Afficher les joueurs du tournois \t \t \t \t 6 -- Générer les paires d'un tour ")
    print("7 -- Afficher les matchs d'un tour \t \t \t \t \t8 -- Mettre à jour le score d'un match  ")
    print("9 -- Retour au menu principal")

nomTournoi = ""
nomTour = ""
joueur1 = ""
joueur2 = ""

def menu_principal():
    global nomTournoi
    option = 0
    while (True):
        try:
            # Vérifier si le dossier "data" existe, sinon le créer
            if not os.path.exists("data"):
                os.mkdir("data")
            # Vérifier si le dossier "tournoi" existe dans "data", sinon le créer
            if not os.path.exists("data/tournaments"):
                os.mkdir("data/tournaments")
            if option == 0:
                print_menu()
                try:
                    option = int(input('\nEntrez votre choix: '))
                except ValueError:
                    print('Erreur. Entrez un numero valide.')
                    option = int(input('\nEntrez votre choix: '))
            if option == 1:
                v = gestion_tournois(option)
                if type(v) == NameError:
                    print('\nSystem erreur : ', v)
                else:
                    nbr_joueur = 0
                    while int(nbr_joueur) < 1:
                        try:
                            nbr_joueur = int(input("Combien de joueurs voulez-vous ajouter ?"))
                            if nbr_joueur > 1 and nbr_joueur % 2 == 0:  # nombre pair
                                for i in range(nbr_joueur):
                                    gestion_joueurs(7)
                                break
                            else:  # nombre impair
                                print('Veuillez saisir un nombre pair')
                                nbr_joueur = 0
                        except Exception:
                            print("Le nombre n'est pas valide.")
                            nbr_joueur = 0
                    t = TournoiController()
                    tournoi = t.get_tournoi(nomTournoi)
                    nbr_tour = tournoi[0]["nbr_tour"]
                    for i in range(nbr_tour):
                        global nomTour
                        nomTour = 'Round ' + str(i+1)
                        gestion_tours(4)  # créer un tour
                        gestion_match(12)  # créer les matchs
                        gestion_match(11)  # afficher les matchs
                        m = MatchController()
                        matchlist = m.get_matchs_by_tour(nomTournoi, nomTour)
                        if type(matchlist) == list:
                            for j in range(len(matchlist)):
                                print('\n' + nomTour + ' - Match ' + str(j+1) + ':')
                                global joueur1
                                joueur1 = matchlist[j]['id_national_1']
                                global joueur2
                                joueur2 = matchlist[j]['id_national_2']
                                gestion_match(10)  # définir un gagnant
                                gestion_match(11)  # afficher les matchs

                        boolChoix = True
                        while(boolChoix):
                            try:
                                option = int(input("Entrez 1 pour fermer le tour sinon 2 pour continuer plus tard : "))
                                if option == 1:
                                    gestion_tours(5)  # fermer le tour
                                    boolChoix = False
                                elif option == 2:
                                    option = 0
                                    boolChoix = False
                                else:
                                    print("Choix invalide, veuillez entrer 1 ou 2 :")
                            except ValueError:
                                print('Choix invalide, veuillez entrer 1 ou 2.')
                        if option == 0:
                            break

            elif option == 2:
                # get nomTournoi
                while len(str(nomTournoi)) < 3:
                    try:
                        nomTournoi = str(input("Veuillez saisir le nom du tournoi : "))
                        if len(str(nomTournoi)) < 3:
                            print("Le nom du tournoi doit contenir au minimum trois caractères.")
                    except Exception:
                        print("Le nom du tournoi n'est pas valide.")
                        nomTournoi = ""
                # get nomTout
                t = Tourcontroller()
                nomTour = t.get_name_current_tour(nomTournoi)

                sous_menu()

                print("Tournoi : "+nomTournoi)

                try:
                    option = int(input('\nEntrez votre choix: '))
                except ValueError:
                    print('Erreur. Entrez un numero valide.')
                    option = int(input('\nEntrez votre choix: '))
                if option == 1:
                    gestion_tournois(3)
                    option = 2

                elif option == 2:
                    if nomTour:
                        gestion_tours(4)
                    else:
                        print('Ce tournoi est fermé, vous ne pouvez pas rajouter de tour')
                    option = 2
                elif option == 3:
                    if nomTour:
                        gestion_tours(5)
                    else:
                        print('Ce tournoi est fermé, tous les tours sont fermés')
                    option = 2

                elif option == 4:
                    gestion_tours(6)
                    option = 2

                elif option == 5:
                    gestion_joueurs(9)
                    option = 2
                elif option == 6:
                    if nomTour:
                        gestion_match(12)
                    else:
                        print('Ce tournoi est fermé, vous ne pouvez pas générer des paires')
                    option = 2
                elif option == 7:
                    gestion_match(11)
                    option = 2
                elif option == 8:
                    if nomTour:
                        m = MatchController()
                        matchlist = m.get_matchs_by_tour(nomTournoi, nomTour)
                        if type(matchlist) == list:
                            for j in range(len(matchlist)):
                                print('\n' + nomTour + ' - Match ' + str(j + 1) + ':')
                                joueur1 = matchlist[j]['id_national_1']
                                joueur2 = matchlist[j]['id_national_2']
                                gestion_match(10)  # définir un gagnant
                        else:
                            print(matchlist)
                    else:
                        print("Ce tournoi est fermé, vous ne pouvez pas mettre à jour les scores")
                    option = 2
                elif option == 9:
                    nomTournoi = ""
                    option = 0
                else:
                    print('Choix invalide, veuillez entrer un numero entre 1 et 9.')
                    option = 2

            elif option == 3:
                gestion_tournois(2)
                option = 0
            elif option == 4:
                gestion_joueurs(8)
                option = 0
            elif option == 5:
                print(MSG_EXIT)
                exit()
            else:
                print('Choix invalide. Veuillez entrer un numero entre 1 et 5.')
                option = 0
        except ValueError:
            print('Choix invalide, veuillez entrer un numero entre 1 et 5.')
            option = 0
