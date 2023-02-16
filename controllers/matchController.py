from controllers.joueurController import joueurController
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
     #creer une fonction de recherche tournoi sur le modelou bien creer un fichier manager model qui contient la fonction
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
                    return "Le nom du tour n'existe pas"
                else:
                    return data_match
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e:
            return e

    """
    Définir le gagnat
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
                        if (match["match"][0]["id_national"] == joueur_1 or match["match"][0]["id_national"] == joueur_2) and (match["match"][1]["id_national"] == joueur_1 or match["match"][1]["id_national"] == joueur_2) :
                            data_match = match
                            if (data_match["match"][0]["id_national"] == joueur_winner) or (data_match["match"][1]["id_national"] == joueur_winner) or (joueur_winner == ""):
                                if(data_match["match"][0]["id_national"] == joueur_winner):
                                    data_match["match"][0]["score"] += 1
                                elif(data_match["match"][1]["id_national"] == joueur_winner):
                                    data_match["match"][1]["score"] += 1
                                else:
                                    data_match["match"][0]["score"] += 0.5
                                    data_match["match"][1]["score"] += 0.5
            if not data_match:
                return "Ces joueur n'ont pas joué de match l'un contre l'autre"
            else:
                with open(a,'w') as jsonfile:
                     json.dump(data, jsonfile)
                return data
        except Exception as e:
            return e
    def generate_paires(self, nom_tournoi):
        # get data des joueurs du tournoi
        j = joueurController()
        data_joueurs = j.get_joueurs_by_tournoi(nom_tournoi)
        #le tri par ordre croissant paar id_national
        joueurs_tries = sorted(data_joueurs, key=lambda joueur: joueur["id_national"])# reverse=True pour le tri décroissant
        for joueur in joueurs_tries:
            (joueur["id_national"], joueur["nom"])

        # generer les paires
        paires = []
        for i in range(0, len(data_joueurs), 2):
            paire = (data_joueurs[i], data_joueurs[i + 1])
            paires.append(paire)

        # Afficher les paires de joueurs
        for paire in paires:
            print(paire[0]["id_national"], "vs", paire[1]["id_national"])




















