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

        def print_menu():
            for key in menu_options.keys():
                print(key, '--', menu_options[key])

        def gestion_tournois():
             sous_tournois  = {

             }

        def gestion_tours():
             print('choisir l option \'Gestion des tours\'')

        def gestion_joueurs():
             print('choisir l option \'Gestion des joueurs\'')

        def gestion_match():
            print('choisir l option \'Gestion des matchs\'')

        if __name__=='__main__':
            while(True):
                print_menu()
                option = ''
                try:
                    option = int(input('Entrer voitre choix: '))
                except:
                    print('Erreur. Entrer un numero ...')
                #Check what choice was entered and act accordingly
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
except Exception as e:
  print(e)