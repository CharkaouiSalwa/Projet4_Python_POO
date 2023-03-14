import json
import os
import random
from collections import defaultdict
from models.match import Match
PATH = "data/tournaments/"


class matchController:
    def __init__(self):
        self
    """
    Retourner la liste des matchs d'un tour
    """
    def get_matchs_by_tour(self, nom_tournoi, nom_tour):
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(nom_tour)) < 3:
                return "Le nom du tour doit contenir au minimum trois caractères."
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
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(nom_tour)) < 3:
                return "Le nom du tour doit contenir au minimum trois caractères."
            if len(str(joueur_1)) != 6:
                return "L'Id national est incorrect"
            if len(str(joueur_2)) != 6:
                return "L'Id national est incorrect"
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
                        if (match["id_national_1"] == joueur_1 or match["id_national_1"] == joueur_2) \
                                and (match["id_national_2"] == joueur_1 or match["id_national_2"] == joueur_2):
                            data_match = match
                            if (data_match["id_national_1"] == joueur_winner) \
                                    or (data_match["id_national_2"] == joueur_winner) \
                                    or (joueur_winner == ""):
                                if data_match["id_national_1"] == joueur_winner:
                                    data_match["score_J1"] += 1
                                elif data_match["id_national_2"] == joueur_winner:
                                    data_match["score_J2"] += 1
                                else:
                                    data_match["score_J1"] += 0.5
                                    data_match["score_J2"] += 0.5
            if not data_match:
                return "Ces joueur n'ont pas joué de match l'un contre l'autre"
            else:
                with open(a, 'w') as jsonfile:
                    json.dump(data, jsonfile)
                return "Le score des joueurs a été mis à jour"
        except Exception as e:
            return e
    """
    retourner data si le tournoi et le tour existent et le tour ne contient pas de match
    """
    def get_data_to_generate(self, nom_tournoi, nom_tour):
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
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
    Créer les matchs d'un tour d'un tournoi
    """
    def creer_matchs(self, nom_tournoi, nom_tour):
        try:
            data = matchController.get_data_to_generate(self,nom_tournoi, nom_tour)
            if data:
                a = PATH + nom_tournoi + '.json'
                if data[0]["tours"][0]["nom_tour"] == nom_tour:
                    if data[0]["tours"][0]["date_heure_fin"]:
                        return 'Ce tour est fermé, vous ne pouvez pas créer des matchs.'
                    data_joueurs = data[0]["joueurs"]
                    data_id_natioanals = []
                    for data_joueur in data_joueurs:
                        data_id_natioanals.append(data_joueur["id_national"])
                    random.shuffle(data_id_natioanals)
                    # generer les paires pour tour[0]
                    paires = matchController.generer_paires_liste(self,data_id_natioanals)
                    for paire in paires:
                        match = Match(paire[0], 0, paire[1], 0)
                        new_data = match.__dict__
                        data[0]["tours"][0]["matchs"].append(new_data)
                        with open(a, 'w') as jsonfile:
                            json.dump(data, jsonfile)
                    return "Les matchs ont été ajoutés avec succès"
                else:
                    # tour 2 tour 3 et tour 4
                    for i in range(1, len(data[0]["tours"])):
                        if data[0]["tours"][i]["nom_tour"] == nom_tour:
                            if data[0]["tours"][i]["date_heure_fin"]:
                                return 'Ce tour est fermé, vous ne pouvez pas créer des matchs.'
                            else:
                                data_matchs_0 = data[0]["tours"][i-1]["matchs"]
                                list_matchs = []
                                for data_match_0 in data_matchs_0:
                                    list_matchs.append([data_match_0["id_national_1"], data_match_0["score_J1"]])
                                    list_matchs.append([data_match_0["id_national_2"], data_match_0["score_J2"]])
                                list_matchs = matchController.calculer_score(self,list_matchs)
                                ma_liste_triee = sorted(list_matchs, key=lambda x: x[1], reverse=True)
                                data_id_natioanals = []
                                data_scores = []
                                for liste_triee in ma_liste_triee:
                                    data_id_natioanals.append(liste_triee[0])
                                    data_scores.append(liste_triee[1])
                                paires_joueurs = matchController.generer_paires_liste(self, data_id_natioanals)
                                paires_score = matchController.generer_paires_liste(self, data_scores)
                                for p in range(len(paires_joueurs)):
                                    match = Match(paires_joueurs[p][0], paires_score[p][0],
                                                  paires_joueurs[p][1], paires_score[p][1])
                                    new_data = match.__dict__
                                    data[0]["tours"][i]["matchs"].append(new_data)
                                    with open(a, 'w') as jsonfile:
                                        json.dump(data, jsonfile)
                                return "Les matchs ont été ajoutés avec succès"
                        else:
                            msg = "Ce tour n'existe pas"
                    return msg
            else:
                return 'Impossible de générer les paires pour ce tour'
        except Exception as e:
            return e
    """
    Generer les paires
    """
    def generer_paires_liste(self, data):
        # Associer les joueurs en paires dans l'ordre
        paires = []
        for i in range(0, len(data), 2):
            if i + 1 < len(data):
                paire = (data[i], data[i + 1])
                paires.append(paire)
        return paires
    """
    Score pour liste de [joueur,score]
    """
    def calculer_score(self, maliste):
        scores = defaultdict(int)
        for joueur, score in maliste:
            scores[joueur] += score
        resultat = [[joueur, score] for joueur, score in scores.items()]
        return resultat
