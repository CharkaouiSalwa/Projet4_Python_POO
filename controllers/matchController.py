from controllers.joueurController import joueurController
from controllers.tournoiController import tournoiController
import itertools
import json,os,random
from itertools import combinations
PATH = "data/tournaments/"

class matchController():
    def __init__(self):
        self
    """
    Retourner la liste des matchs d'un tour
    """
     #creer une fonction de recherche tournoi sur le model ou bien creer un fichier manager model qui contient la fonction
     #deux fonctions une de lecture et l'autre de l'ecriture sur un fichier model tour_manager
     # passer flake8 pour corriger les erreurs
    def get_matchs_by_tour(self, nom_tournoi, nom_tour):
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(nom_tour)) < 3:
                return "Le nom du tour doit contenir au minimum trois caractères."
            data = []
            data_match = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                    for i in data[0]["tours"]:
                        if i["nom_tour"] == nom_tour:
                            data_match = i["matchs"]
                if not data_match:
                    return "Ce tour ne contient pas de matchs"
                else:
                    return data_match
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e:
            return e

    """
    Définir le gagnant
    """
    def match_winner(self, nom_tournoi, nom_tour, joueur_1, joueur_2, joueur_winner):
        try :
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(nom_tour)) < 3:
                return "Le nom du tour doit contenir au minimum trois caractères."
            if len(str(joueur_1)) != 6:
                return "L'Id national est incorrect"
            if len(str(joueur_2)) != 6:
                return "L'Id national est incorrect"
            data = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
            else:
                return "Le nom de tournoi n'existe pas"

            data_tours = data[0]["tours"]
            data_matchs = []
            data_match = []
            for data_tour in data_tours:
                if data_tour["nom_tour"] == nom_tour:
                    data_matchs = data_tour["matchs"]
                    for match in data_matchs:
                        if (match["id_national_1"] == joueur_1 or match["id_national_1"] == joueur_2) and (match["id_national_2"] == joueur_1 or match["id_national_2"] == joueur_2) :
                            data_match = match
                            if (data_match["id_national_1"] == joueur_winner) or (data_match["id_national_2"] == joueur_winner) or (joueur_winner == ""):
                                if(data_match["id_national_1"] == joueur_winner):
                                    data_match["score_J1"] += 1
                                elif(data_match["id_national_2"] == joueur_winner):
                                    data_match["score_J2"] += 1
                                else:
                                    data_match["score_J1"] += 0.5
                                    data_match["score_J2"] += 0.5
            if not data_match:
                return "Ces joueur n'ont pas joué de match l'un contre l'autre"
            else:
                with open(a,'w') as jsonfile:
                     json.dump(data, jsonfile)
                return "Le score des joueurs a été mis à jour"
        except Exception as e:
            return e

    """
    retourner data si le tournoi et le tour existent et le tour ne contient pas de match
    else return None 
    """

    def get_data_to_generate(self, nom_tournoi, nom_tour):
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            data = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                    tours = data[0]['tours']
                    data_tour = []
                    data_match = []
                    for tour in tours:
                        # tour exist
                        if tour["nom_tour"] == nom_tour:
                            data_tour = tour["nom_tour"]
                            # cas des paires sont generées
                            if tour["matchs"]:
                                data_match = tour["matchs"]
                if data_tour and not data_match:
                    return data
                else:
                    return None
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e:
            return e

    """
    Generer les paires des joueurs d'un tour
    """
    def generate_paires(self, nom_tournoi, nom_tour):
        data = self.get_data_to_generate(nom_tournoi,nom_tour)
        if data :
            if(data[0]["tours"][0]["nom_tour"] == nom_tour):
                data_joueurs = data[0]["joueurs"]
                data_id_natioanals = []
                for data_joueur in data_joueurs:
                    data_id_natioanals.append(data_joueur["id_national"])

                random.shuffle(data_id_natioanals)
                #generer les paires pour tour[0]
                # generer les paires
                paires = []
                for i in range(0, len(data_id_natioanals), 2):
                    paire = (data_id_natioanals[i], data_id_natioanals[i + 1])
                    paires.append(paire)
                # Afficher les paires de joueurs
                for paire in paires:
                    print(paire[0], "vs", paire[1])
            else :
                print('ko')

        else: #ne pas generer
            return 'Impossible de générer les paires pour ce tour'

    """
    Trier les joueurs par id_national
    """
    def trie_id_national(self,nom_tournoi):
        # get data des joueurs du tournoi
        j = joueurController()
        data_joueurs = j.get_joueurs_by_tournoi(nom_tournoi)
        # le tri par ordre croissant par id_national
        joueurs_tries = sorted(data_joueurs,key=lambda joueur: joueur["id_national"])  # reverse=True pour le tri décroissant
        return joueurs_tries

    """
    
    """