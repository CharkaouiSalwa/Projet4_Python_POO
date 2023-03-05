from views.tournoiView import tournoiView
from views.joueurView import JoueurView
from views.tourView import tourView
from views.matchView import matchView
MSG_EXIT = 'Merci pour votre visite, à bientot !'


sous_tournois = {
    1: 'Ajouter un tournoi',
    2: 'Afficher tous les tournois',
    3: 'Afficher nom et date du tournois'
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
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 13.')


sous_tours = {
    4: 'Ajouter un tour',
    5: 'Fermer un tour',
    6: 'Afficher les tours du tournois'
}


def gestion_tours(option):
    while (True):
        try:
            option
        except ValueError:
            print('Erreur. Entrer un numero ...')
        # Check what choice was entered and act accordingly
        if option == 4:
            t = tourView()
            return t.ajouter_tour()
        elif option == 5:
            t = tourView()
            return t.fermer_tour()
        elif option == 6:
            t = tourView()
            return t.afficher_tours_du_tournoi()
        else:
            print('Option invalide. Veuillez entrer un numero entre 1 et 13.')


sous_joueurs = {
    7: 'Ajouter un joueur',
    8: 'Afficher tous les joueurs',
    9: 'Afficher les joueurs du tournois'
}


def gestion_joueurs(option):
    while (True):
        try:
            option
        except ValueError:
            print('Erreur. Entrer un numero ...')
        if option == 7:
            t = JoueurView()
            return t.add_joueur()
        elif option == 8:
            t = JoueurView()
            return t.afficher_joueurs()
        elif option == 9:
            t = JoueurView()
            return t.afficher_joueurs_tournoi()
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 13.')


sous_match = {
    10: "Mettre à jour le score d'un match",
    11: "Afficher les matchs d'un tour",
    12: "Générer les paires d'un tour"
}


def gestion_match(option):
    while (True):
        try:
            option
        except ValueError:
            print('Erreur. Entrer un numero ...')
        if option == 10:
            m = matchView()
            return m.gagnant()
        elif option == 11:
            m = matchView()
            return m.afficher_matchs_by_tour()
        elif option == 12:
            m = matchView()
            return m.create_match()
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 13.')
