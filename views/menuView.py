from controllers.menuController import gestion_tournois, gestion_tours,\
                                       gestion_joueurs
from controllers.tourController import Tourcontroller
from controllers.menuController import MSG_EXIT, joueurs_exist, \
    ajouter_joueurs, get_nbr_tour, new_or_continu_tournoi, get_tour_actuel
import os


def print_menu():

    print("1 -- Ajouter un nouveau tournoi")
    print("2 -- Continuer un tournoi")
    print("3 -- Afficher tous les tournois")
    print("4 -- Afficher tous les joueurs")
    print("5 -- Quitter")


nomTournoi = ""
nomTour = ""
joueur1 = ""
joueur2 = ""


def menu_principal():
    # Vérifier si le dossier "data" existe, sinon le créer
    if not os.path.exists("data"):
        os.mkdir("data")
    # Vérifier si le dossier "tournoi" existe dans "data", sinon le créer
    if not os.path.exists("data/tournaments"):
        os.mkdir("data/tournaments")
    global nomTournoi
    option = 0
    while (True):
        try:

            if option == 0:
                nomTournoi = ''
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
                    ajouter_joueurs()
                    nbr_tour = get_nbr_tour(nomTournoi)
                    tour_actuel = 0
                    new_or_continu_tournoi(nomTournoi, nbr_tour, tour_actuel)
                option = 0
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
                # get nomTour
                t = Tourcontroller()
                global nomTour
                nomTour = t.get_name_current_tour(nomTournoi)
                if nomTour == "Le nom de tournoi n'existe pas" or\
                        nomTour == 'Vous ne pouvez pas continuer un tournoi fermé':
                    print("Erreur : ", nomTour)
                    nomTournoi = ""
                    option = 0
                else:
                    print("Tournoi : "+nomTournoi)
                    if not joueurs_exist(nomTournoi):
                        ajouter_joueurs()
                    nbr_tour = get_nbr_tour(nomTournoi)
                    tour_actuel = get_tour_actuel(nomTournoi)
                    if nbr_tour == tour_actuel:
                        gestion_tours(5)
                    else:
                        new_or_continu_tournoi(nomTournoi, nbr_tour, tour_actuel)
                    option = 0

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
