# run menu
try:
    if __name__ == "__main__":
        menu_options = {
            1: 'Gestion des tournois',
            2: 'Gestion des tours',
            3: 'Gestion des joueurs',
            4: 'Gestion des matchs',
            5: 'Quitter'
        }
        sous_tournois = {
            1: 'Ajouter un tournoi',
            2: 'Afficher tous les tournois',
            3: 'Afficher nom et date du tournois',
            4: 'Retour au menu principal',
            5: 'Quitter'
        }
        sous_tours = {
            1: 'Ajouter un tour',
            2: 'Fermer un tour',
            3: 'Afficher les tours du tournois',
            4: 'Retour au menu principal',
            5: 'Quitter'

        }
        sous_joueurs = {
            1: 'Ajouter un joueur',
            2: 'Afficher tous les joueurs',
            3: 'Afficher les joueurs du tournois',
            4: 'Retour au menu principal',
            5: 'Quitter'
        }
        sous_match = {
            1: 'Definir un gagnant',
            2: 'Afficher les matchs d un tour',
            3: 'Retour au menu principal',
            4: 'Quitter'
        }

        def print_menu(menu):
            for key in menu_options.keys():
                print(key, '--', menu[key])
        def menu_principal():
            while (True):
                print_menu(menu_options)
                option = ''
                try:
                    option = int(input('Entrer voitre choix: '))
                except:
                    print('Erreur. Entrer un numero ...')
                # Check what choice was entered and act accordingly
                if option == 1:
                    gestion_tournois()
                elif option == 2:
                    gestion_tours()
                elif option == 3:
                    gestion_joueurs()
                elif option == 4:
                    gestion_match()
                elif option == 5:
                    print('Merci pour votre visite, à bientot !')
                    exit()
                else:
                    print('Option ivalide. Svp entrer un numero entre 1 et 5.')

        def gestion_tournois():
            while (True):
                print_menu(sous_tournois)
                option = ''
                try:
                    option = int(input('Entrer voitre choix: '))
                except:
                    print('Erreur. Entrer un numero ...')
                # Check what choice was entered and act accordingly
                if option == 1:
                   print('ajouter un tournoi')
                elif option == 2:
                    print('Afficher tous les tournois')
                elif option == 3:
                    print('Afficher nom et date du tournois')
                elif option == 4:
                   menu_principal()
                elif option == 5:
                    print('Merci pour votre visite, à bientot !')
                    exit()
                else:
                    print('Option ivalide. Svp entrer un numero entre 1 et 5.')

        def gestion_tours():
            while (True):
                print_menu(sous_tours)
                option = ''
                try:
                    option = int(input('Entrer voitre choix: '))
                except:
                    print('Erreur. Entrer un numero ...')
                # Check what choice was entered and act accordingly
                if option == 1:
                    print('ajouter un tour')
                elif option == 2:
                    print('Fermer un tour ')
                elif option == 3:
                    print('Afficher les tours du tournois')
                elif option == 4:
                    menu_principal()
                elif option == 5:
                    print('Merci pour votre visite, à bientot !')
                    exit()
                else:
                    print('Option ivalide. Svp entrer un numero entre 1 et 5.')

        def gestion_joueurs():
            while (True):
                print_menu(sous_joueurs)
                option = ''
                try:
                    option = int(input('Entrer voitre choix: '))
                except:
                    print('Erreur. Entrer un numero ...')
                # Check what choice was entered and act accordingly
                if option == 1:
                    print('ajouter un joueur')
                elif option == 2:
                    print('Afficher tous les joueurs')
                elif option == 3:
                    print('Afficher les joueurs du tournois')
                elif option == 4:
                    menu_principal()
                elif option == 5:
                    print('Merci pour votre visite, à bientot !')
                    exit()
                else:
                    print('Option ivalide. Svp entrer un numero entre 1 et 5.')

        def gestion_match():
            while (True):
                print_menu(sous_match)
                option = ''
                try:
                    option = int(input('Entrer voitre choix: '))
                except:
                    print('Erreur. Entrer un numero ...')
                # Check what choice was entered and act accordingly
                if option == 1:
                    print('definir un gagnant')
                elif option == 2:
                    print('Afficher les matchs d un tour')
                elif option == 3:
                    menu_principal()
                elif option == 4:
                    print('Merci pour votre visite, à bientot !')
                    exit()
                else:
                    print('Option ivalide. Svp entrer un numero entre 1 et 4.')
        if __name__=='__main__':
            menu_principal()

except Exception as e:1
  print(e)