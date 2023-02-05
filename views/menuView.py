from controllers.menuController import gestion_tournois,sous_tournois,sous_tours,gestion_tours,sous_joueurs,\
                                       gestion_joueurs,sous_match,gestion_match
from controllers.menuController import MSG_MENU_PRINCIPAL
from controllers.menuController import MSG_EXIT

menu_options = {
    1: 'Gestion des tournois',
    2: 'Gestion des tours',
    3: 'Gestion des joueurs',
    4: 'Gestion des matchs',
    5: 'Quitter'
}

def print_menu(menu):
    for key in menu.keys():
        print(key, '--', menu[key])

def menu_principal():
    while (True):
        print_menu(menu_options)
        option = ''
        try:
          option = int(input('Entrez votre choix: '))
        except:
          print('Erreur. Entrez un numero valide.')
        # Check what choice was entered and act accordingly
        if option == 1:
            print_menu(sous_tournois)
            option2 = int(input('Entrez votre choix: '))
            msg = gestion_tournois(option2)
            print(msg)
            if(msg == MSG_EXIT):
                exit()
            elif(msg == MSG_MENU_PRINCIPAL):
                menu_principal()
        elif option == 2:
            print_menu(sous_tours)
            option2 = int(input('Entrez votre choix: '))
            msg = gestion_tours(option2)
            print(msg)
            if (msg == MSG_EXIT):
                exit()
            elif (msg == MSG_MENU_PRINCIPAL):
                menu_principal()
        elif option == 3:
            print_menu(sous_joueurs)
            option2 = int(input('Entrez votre choix: '))
            msg = gestion_joueurs(option2)
            print(msg)
            if (msg == MSG_EXIT):
                exit()
            elif (msg == MSG_MENU_PRINCIPAL):
                menu_principal()
        elif option == 4:
            print_menu(sous_match)
            option2 = int(input('Entrez votre choix: '))
            msg = gestion_match(option2)
            print(msg)
            if (msg == MSG_EXIT):
                exit()
            elif (msg == MSG_MENU_PRINCIPAL):
                menu_principal()
        elif option == 5:
            print(MSG_EXIT)
            exit()
        else:
            print('Option invalide. Veuillez entrer un numero entre 1 et 5.')




