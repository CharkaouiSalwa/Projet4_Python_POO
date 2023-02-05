from views.tournoiView import tournoiView
MSG_MENU_PRINCIPAL = 'Menu Principal'
MSG_EXIT = 'Merci pour votre visite, à bientot !'

##sous menu tournoi
sous_tournois = {
    1: 'Ajouter un tournoi',
    2: 'Afficher tous les tournois',
    3: 'Afficher nom et date du tournois',
    4: 'Retour au menu principal',
    5: 'Quitter'
}

def gestion_tournois(option):
    while (True):
        try:
             option
        except:
            return ('Erreur. Entrer un numero ...')
        # Check what choice was entered and act accordingly
        if option == 1:
           t= tournoiView()
           return t.ajoutertournoi()
        elif option == 2:
            return ('Afficher tous les tournois')
        elif option == 3:
            return ('Afficher nom et date du tournois')
        elif option == 4:
            return MSG_MENU_PRINCIPAL
        elif option == 5:
            return MSG_EXIT
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 5.')


#sous menu tour
sous_tours = {
    1: 'Ajouter un tour',
    2: 'Fermer un tour',
    3: 'Afficher les tours du tournois',
    4: 'Retour au menu principal',
    5: 'Quitter'
}
def gestion_tours(option):
    while (True):
        try:
            option
        except:
            print('Erreur. Entrer un numero ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            return ('ajouter un tour')
        elif option == 2:
            return ('Fermer un tour ')
        elif option == 3:
            return ('Afficher les tours du tournois')
        elif option == 4:
            return MSG_MENU_PRINCIPAL
        elif option == 5:
            return MSG_EXIT
        else:
            print('Option invalide. Veuillez entrer un numero entre 1 et 5.')


#sous menu joueur
sous_joueurs = {
    1: 'Ajouter un joueur',
    2: 'Afficher tous les joueurs',
    3: 'Afficher les joueurs du tournois',
    4: 'Retour au menu principal',
    5: 'Quitter'
}
def gestion_joueurs(option):
    while (True):
        try:
            option
        except:
            print('Erreur. Entrer un numero ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            return('ajouter un joueur')
        elif option == 2:
            return ('Afficher tous les joueurs')
        elif option == 3:
            return ('Afficher les joueurs du tournois')
        elif option == 4:
            return MSG_MENU_PRINCIPAL
        elif option == 5:
            return MSG_EXIT
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 5 .')

#sous menu match
sous_match = {
    1: 'Definir un gagnant',
    2: 'Afficher les matchs d un tour',
    3: 'Retour au menu principal',
    4: 'Quitter'
}

def gestion_match(option):
    while (True):
        try:
            option
        except:
            print('Erreur. Entrer un numero ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            return ('definir un gagnant')
        elif option == 2:
            return ('Afficher les matchs d un tour')
        elif option == 3:
             return MSG_MENU_PRINCIPAL
        elif option == 4:
            return MSG_EXIT
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 4.')



