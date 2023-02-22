from views.tournoiView import tournoiView
from views.joueurView import JoueurView
from views.tourView import tourView
from views.matchView import matchView
MSG_MENU_PRINCIPAL = 'Menu Principal'
MSG_EXIT = 'Merci pour votre visite, à bientot !'


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
        except ValueError:
            return ('Erreur. Entrer un numero ...')
        if option == 1:
            t = tournoiView()
            return t.ajoutertournoi()
        elif option == 2:
            t = tournoiView()
            return t.afficher_tournois()
        elif option == 3:
            t = tournoiView()
            return t.afficher_nom_date_tournoi()
        elif option == 4:
            return MSG_MENU_PRINCIPAL
        elif option == 5:
            return MSG_EXIT
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 5.')


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
        except ValueError:
            print('Erreur. Entrer un numero ...')
        # Check what choice was entered and act accordingly
        if option == 1:
            t = tourView()
            return t.ajouter_tour()
        elif option == 2:
            t = tourView()
            return t.fermer_tour()
        elif option == 3:
            t = tourView()
            return t.afficher_tours_du_tournoi()
        elif option == 4:
            return MSG_MENU_PRINCIPAL
        elif option == 5:
            return MSG_EXIT
        else:
            print('Option invalide. Veuillez entrer un numero entre 1 et 5.')


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
        except ValueError:
            print('Erreur. Entrer un numero ...')
        if option == 1:
            t = JoueurView()
            return t.add_joueur()
        elif option == 2:
            t = JoueurView()
            return t.afficher_joueurs()
        elif option == 3:
            t = JoueurView()
            return t.afficher_joueurs_tournoi()
        elif option == 4:
            return MSG_MENU_PRINCIPAL
        elif option == 5:
            return MSG_EXIT
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 5 .')


sous_match = {
    1: "Definir un gagnant d'un match",
    2: "Afficher les matchs d'un tour",
    3: "Générer les paires d'un tour",
    4: "Retour au menu principal",
    5: 'Quitter'
}


def gestion_match(option):
    while (True):
        try:
            option
        except ValueError:
            print('Erreur. Entrer un numero ...')
        if option == 1:
            m = matchView()
            return m.gagnant()
        elif option == 2:
            m = matchView()
            return m.afficher_matchs_by_tour()
        elif option == 3:
            m = matchView()
            return m.create_match()
        elif option == 4:
            return MSG_MENU_PRINCIPAL
        elif option == 5:
            return MSG_EXIT
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 4.')
