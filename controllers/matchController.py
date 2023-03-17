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
                if data_tour:
                    if not data_match:
                        return data
                    else:
                        return "Les matchs sont déjà générés pour ce tour"
                else:
                    return "Ce tour n'existe pas, impossible de générer des matchs pour ce tour"
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
            if type(data) == list:
                a = PATH + nom_tournoi + '.json'
                if data[0]["tours"][0]["nom_tour"] == nom_tour:
                    if data[0]["tours"][0]["date_heure_fin"]:
                        return 'Ce tour est fermé, vous ne pouvez pas créer des matchs.'
                    data_joueurs = data[0]["joueurs"]
                    data_id_natioanals = []
                    for data_joueur in data_joueurs:
                        data_id_natioanals.append(data_joueur["id_national"])
                    # generer les paires pour tour[0]
                    for i in range(0, len(data_id_natioanals), 2):
                        match = Match(data_id_natioanals[i], 0, data_id_natioanals[i+1], 0)
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
                                list_matchs_prec = []
                                for data_match_0 in data_matchs_0:
                                    list_matchs_prec.append([data_match_0["id_national_1"], data_match_0["score_J1"]])
                                    list_matchs_prec.append([data_match_0["id_national_2"], data_match_0["score_J2"]])
                                list_matchs_prec = matchController.calculer_score(self,list_matchs_prec)
                                ma_liste_triee = sorted(list_matchs_prec, key=lambda x: x[1], reverse=True)
                                final_list_paires = matchController.generation_paires(self,list_matchs_prec,ma_liste_triee)
                                if type(final_list_paires) == list:
                                    for p in range(0,len(final_list_paires),2):
                                        match = Match(final_list_paires[p][0], final_list_paires[p][1],
                                                      final_list_paires[p+1][0], final_list_paires[p+1][1])
                                        new_data = match.__dict__
                                        data[0]["tours"][i]["matchs"].append(new_data)
                                        with open(a, 'w') as jsonfile:
                                            json.dump(data, jsonfile)
                                    return "Les matchs ont été ajoutés avec succès"
                                else:
                                    return final_list_paires
                        else:
                            msg = "Ce tour n'existe pas"
                    return msg
            else:
                return data
        except Exception as e:
            return e

    """
    Score pour liste de [joueur,score]
    """
    def calculer_score(self, maliste):
        try:
            scores = defaultdict(int)
            for joueur, score in maliste:
                scores[joueur] += score
            resultat = [[joueur, score] for joueur, score in scores.items()]
            return resultat
        except Exception:
            return None

    """
    Generer des paires
    """
    def generation_paires(self, list_matchs_prec, ma_liste_triee):
        try:
            if list_matchs_prec == []:
                return ma_liste_triee
            else:
                if list_matchs_prec == ma_liste_triee:
                    new_list = []
                    n = len(list_matchs_prec)
                    for i in range(n // 2):
                        new_list.append(ma_liste_triee[i])
                        new_list.append(ma_liste_triee[n - i - 1])
                    if n % 2 != 0:
                        new_list.append(ma_liste_triee[n // 2])
                    return new_list
                else:
                    # Si les deux listes sont différentes, on retourne la liste triée
                    return ma_liste_triee
        except Exception as e:
            return e