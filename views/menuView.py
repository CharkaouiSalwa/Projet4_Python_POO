from controllers.menuController import gestion_tournois, gestion_tours,\
                                       gestion_joueurs, gestion_match
from controllers.menuController import MSG_EXIT
import os


def print_menu():
    print("1 -- Ajouter un tournoi \t \t \t \t \t \t \t 2 -- Afficher tous les tournois")
    print("3 -- Afficher nom et date du tournois \t \t \t \t 4 -- Ajouter un tour")
    print("5 -- Fermer un tour \t \t \t \t \t \t \t \t 6 -- Afficher les tours du tournois")
    print("7 -- Ajouter un joueur \t \t \t \t \t \t \t \t 8 -- Afficher tous les joueurs")
    print("9 -- Afficher les joueurs du tournois \t \t \t \t 10 -- Definir un gagnant d'un match")
    print("11 -- Afficher les matchs d'un tour \t \t \t \t 12 -- Générer les paires d'un tour")
    print("13 -- Quitter")

nomTournoi = ""
nomTour = ""

def menu_principal():
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
            if option == 1 or option == 2 or option == 3:
                v = gestion_tournois(option)
                if type(v) == NameError:
                    print('\nSystem erreur : ', v)
                    break
                else:
                    if option == 1:
                        boolAddJoueur = True
                        while (boolAddJoueur):
                            print("Voulez-vous ajouter des joueurs à ce tournoi ?")
                            option = int(input("Entrez 1 pour oui sinon entrez 2: "))
                            if option == 1:
                                gestion_joueurs(7)
                            elif option == 2:
                                boolAddJoueur = False
                                boolAddTour = True
                                while(boolAddTour):
                                    option = int(input("Entrez 1 pour ajouter un tour sinon 2 pour afficher le menu : "))
                                    if option == 1:
                                        gestion_tours(4)
                                        option = int(input("Entrez 1 pour generer les paires sinon 2 pour afficher le menu : "))
                                        if option == 1:
                                            gestion_match(12)
                                            option = int(input("Entrez 1 pour afficher les matchs sinon 2 pour afficher le menu : "))
                                            if option == 1:
                                                while(True):
                                                    gestion_match(11)
                                                    option = int(input("Entrez 1 pour mettre à jour les scores ou 2"
                                                                       " pour fermer le tour sinon 3 pour afficher le menu : "))
                                                    if option == 1:
                                                        gestion_match(10)
                                                    elif option == 2:
                                                        gestion_tours(5)
                                                        break
                                                    else:
                                                        option = 0
                                                        break
                                            else:
                                                option = 0
                                                break
                                        else:
                                            option = 0
                                            break
                                    elif option == 2:
                                        option = 0
                                        boolAddTour = False
                                    else:
                                        option = int(input("Entrez 0 pour afficher le menu sinon entrez 13 pour quitter: "))
                                        boolAddTour = False
                            else:
                                option = int(input("Entrez 0 pour afficher le menu sinon entrez 13 pour quitter: "))
                                boolAddJoueur = False
                    else:
                        option = int(input("Entrez 0 pour afficher le menu sinon entrez 13 pour quitter: "))

            elif option == 4 or option == 5 or option == 6:
                gestion_tours(option)
                option = int(input("Entrez 0 pour afficher le menu sinon entrez 13 pour quitter: "))
            elif option == 7 or option == 8 or option == 9:
                gestion_joueurs(option)
                option = int(input("Entrez 0 pour afficher le menu entrez 13 pour quitter: "))
            elif option == 10 or option == 11 or option == 12:
                gestion_match(option)
                option = int(input("Entrez 0 pour afficher le menu entrez 13 pour quitter: "))
            elif option == 13:
                print(MSG_EXIT)
                exit()
            else:
                print('Option invalide. Veuillez entrer un numero entre 1 et 13.')
                option = 0
        except ValueError:
            print('Choix invalide, veuillez entrer un numero entre 1 et 13.')
            option = 0
