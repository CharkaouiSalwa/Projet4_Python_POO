from views.tournoiView import TournoiView
from views.joueurView import JoueurView
from views.tourView import TourView
from views.matchView import MatchView
from controllers.tournoiController import TournoiController
from controllers.matchController import MatchController
import views.menuView
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
            t = TournoiView()
            return t.ajoutertournoi()
        elif option == 2:
            t = TournoiView()
            return t.afficher_tournois()
        elif option == 3:
            t = TournoiView()
            return t.afficher_nom_date_tournoi()
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 13.')


def joueurs_exist(nom_tournoi):
    t = TournoiController()
    data = t.get_tournoi(nom_tournoi)
    if data[0]["joueurs"]:
        return True
    else:
        return False


def ajouter_joueurs():
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


def get_nbr_tour(nom_tournoi):
    t = TournoiController()
    tournoi = t.get_tournoi(nom_tournoi)
    return tournoi[0]["nbr_tour"]


def get_tour_actuel(nom_tournoi):
    t = TournoiController()
    tournoi = t.get_tournoi(nom_tournoi)
    return tournoi[0]["tour_actuel"]


def check_tour_prec_ferme(nom_tournoi, tour_actuel):
    t = TournoiController()
    data = t.get_tournoi(nom_tournoi)
    tours = data[0]["tours"]
    if not tours[tour_actuel - 1]["date_heure_fin"]:  # tour pas fermer
        return False
    else:
        return True


def new_or_continu_tournoi(nom_tournoi, nbr_tour, tour_actuel):
    for i in range(tour_actuel, nbr_tour):
        if tour_actuel:
            if not check_tour_prec_ferme(nom_tournoi, tour_actuel):
                views.menuView.nomTour = 'Round ' + str(i)
                gestion_tours(5)  # fermer le tour
        views.menuView.nomTour = 'Round ' + str(i + 1)
        gestion_tours(4)  # créer un tour
        gestion_match(12)  # créer les matchs
        gestion_match(11)  # afficher les matchs
        m = MatchController()
        matchlist = m.get_matchs_by_tour(nom_tournoi, views.menuView.nomTour)
        if type(matchlist) == list:
            for j in range(len(matchlist)):
                print('\n' + views.menuView.nomTour + ' - Match ' + str(j + 1) + ':')
                views.menuView.joueur1 = matchlist[j]['id_national_1']
                views.menuView.joueur2 = matchlist[j]['id_national_2']
                gestion_match(10)  # définir un gagnant
                gestion_match(11)  # afficher les matchs

        boolChoix = True
        while (boolChoix):
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
            t = TourView()
            return t.ajouter_tour()
        elif option == 5:
            t = TourView()
            return t.fermer_tour()
        elif option == 6:
            t = TourView()
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
            m = MatchView()
            return m.gagnant()
        elif option == 11:
            m = MatchView()
            return m.afficher_matchs_by_tour()
        elif option == 12:
            m = MatchView()
            return m.create_match()
        else:
            return ('Option invalide. Veuillez entrer un numero entre 1 et 13.')
