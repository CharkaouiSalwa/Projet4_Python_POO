from models.match import Match
from controllers.joueurController import joueurController
import json,os,io
PATH = "data/tournaments/"
class matchController:
    def __init__(self):
        self
    """
    Retourner la liste des matchs d'un tour
    """
    def get_matchs_by_tour(self,nom_tournoi,nom_tour):
        #get data
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
                if data_match == [] :
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
            #if len(str(joueur_winner)) != 6:
               # return "L'Id national est incorrect"
            data = []
            data_matchs= []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                    for i in data[0]["tours"]:
                        if i["nom_tour"] == nom_tour:
                            data_matchs = i["matchs"]
                if data_matchs == []:
                    return "Le nom du tour n'existe pas"
                else:
                    data_match = []
                    i=0
                    for i in data_matchs:
                       # for b in data_matchs[0]["match"][0]["id_national"]:

                       if (data_matchs[0]["match"][0]["id_national"] == joueur_1) or (data_matchs[0]["match"][0]["id_national"]==joueur_2):
                                #if joueur_winner == "":
                                if  joueur_winner == joueur_1:
                                    i["match"][0]["score"] += 1
                                if joueur_winner == joueur_2:
                                    i["match"][1]["score"] += 1
                                else:
                                    i["match"][0]["score"] += 0.5
                                    i["match"][1]["score"] += 0.5


                    with open(a,'w') as jsonfile:
                        json.dump(data_matchs, jsonfile)
                        return "Le gangant est le joueur", joueur_winner
            else:
                return "Le nom de tournoi n'existe pas"


        except Exception as e:
            return e





    def generate_paires(self,nom_tournoi,nom_tour):
        #get data des joueurs du tournoi
        j = joueurController()
        data_joueurs = j.get_joueurs_by_tournoi(nom_tournoi)
        #generer des paires pour les joueurs
        return data_joueurs




