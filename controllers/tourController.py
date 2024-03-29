from models.tour import Tour
import json
import os
from datetime import datetime
PATH = "data/tournaments/"


class Tourcontroller:
    def __init__(self):
        self

    def add_tour(self, nom_tournoi, nom_tour):
        """Ajouter un tour dans une tournois"""
        try:
            if len(str(nom_tour)) < 3:
                return "Le nom doit contenir au minimum trois caractères."
            tours = Tour(nom_tour)
            a = PATH + nom_tournoi + '.json'
            if os.path.isfile(a):  # check if file exist
                with open(a, "r") as jsonfile:  # read and write in file
                    data = json.load(jsonfile)
                new_data = tours.__dict__
                tour_actuel = data[0]["tour_actuel"]
                # if tour_actuel == 4:
                #   return "Vous ne pouvez avoir plus de 4 tours"
                if len(data[0]["tours"]) == 0:
                    data[0]["tours"].append(new_data)
                    data[0]["tour_actuel"] += 1
                else:
                    tours = data[0]["tours"]
                    for tour in tours:
                        if tour["nom_tour"] == nom_tour:
                            return 'Ce nom tour existe déja, veuillez fermer le tour'
                    if tours[tour_actuel-1]["date_heure_fin"]:
                        data[0]["tours"].append(new_data)
                        data[0]["tour_actuel"] += 1
                    else:
                        return "Veuillez fermer le tour précédent avant de rajouter un nouveau tour."
                with open(a, 'w') as jsonfile:
                    json.dump(data, jsonfile)
                return "Le tour a été ajouté avec succès"
            else:
                return "Le nom du tournoi n'existe pas"
        except Exception as e:
            return e

    def get_tours_by_tournoi(self, nom_tournoi):
        """retourner tous les tours d'un tournoi"""
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            a = PATH + nom_tournoi + '.json'
            if os.path.isfile(a):  # check if file exist
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                return data[0]['tours']
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e:
            return e

    def close_tour(self, nom_tournoi, nom_tour):
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(nom_tour)) < 3:
                return "Le nom du tour doit contenir au minimum trois caractères."
            a = PATH + nom_tournoi + '.json'
            if os.path.isfile(a):  # check if file exist
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                msg = ""
                tourFerme = False
                tourExist = False
                for i in range(0, len(data[0]["tours"])):
                    if data[0]["tours"][i]["nom_tour"] == nom_tour:
                        tourExist = True
                        if data[0]["tours"][i]["date_heure_fin"] == "":
                            db = datetime.today()
                            data[0]["tours"][i]["date_heure_fin"] = db.strftime("%d/%m/%Y %H:%M:%S")
                            tourFerme = True
                            if i == data[0]["nbr_tour"]-1:
                                data[0]["date_fin"] = db.strftime("%d/%m/%Y %H:%M:%S")
                                msg = ", le tournoi est fermé dans ce dernier tour"
                if not tourFerme:
                    return 'Le tour est déjà fermé'
                elif not tourExist:
                    return "Ce tour n'existe pas, veuillez ajouter le tour"
                else:
                    with open(a, 'w') as jsonfile:
                        json.dump(data, jsonfile)
                        return "Le tour a été fermé avec succès"+msg
            else:
                return "Le tournoi n'existe pas"
        except Exception as e:
            return e

    def get_name_current_tour(self, nom_tournoi):
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            a = PATH + nom_tournoi + '.json'
            if os.path.isfile(a):  # check if file exist
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                nom_tour = ""
                for i in range(0, len(data[0]["tours"])):
                    if data[0]["tours"][i]["date_heure_fin"] == "":
                        nom_tour = data[0]["tours"][i]["nom_tour"]
                    else:
                        if data[0]["date_fin"] == "":
                            # generer nouveau round
                            nom_tour = 'Round ' + str(int(data[0]["tour_actuel"])+1)
                        else:
                            nom_tour = "Vous ne pouvez pas continuer un tournoi fermé"
                return nom_tour
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e:
            return e
