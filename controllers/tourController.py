from models.tour import Tour
import uuid
import json,os,io
from datetime import date,datetime
PATH = "data/tournaments/"
class tourcontroller :
    def __init__(self):
        self

    """
    Ajouter un tour dans une tournois
    """
    def add_tour(self,nom_tournoi, nom_tour):
        try:

            if len(str(nom_tour)) < 3:
                return "Le nom doit contenir au minimum trois caractères."

            tours = Tour(nom_tour)
            data = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                # read and write in file
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                new_data = tours.__dict__
                data[0]["tours"].append(new_data)
                with open(a, 'w') as jsonfile:
                    json.dump(data, jsonfile)

                return data
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e:
            return e



    """
        retourner tous les tours d'un tournoi
        """

    def get_tours_by_tournoi(self, nom_tournoi):
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            data = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                return (data[0]['tours'])
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e :
            return e

        """
        Fermer un tour 
        """
    def close_tour(self,nom_tournoi,nom_tour):
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(nom_tour)) < 3:
                return "Le nom du tour doit contenir au minimum trois caractères."
            new_data = []
            data = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                for i in data[0]["tours"]:
                    if i["nom_tour"] == nom_tour:
                        if i["date_heure_fin"] == "":
                            db = datetime.today()
                            i["date_heure_fin"] = db.strftime("%d/%m/%Y %H:%M:%S")
                        else :
                            return 'Le tour est déjà fermé'
                with open(a,'w') as jsonfile:
                    json.dump(data, jsonfile)
                    return "Le tour a été fermé avec succès"



            else:
                return "Le tournoi n'existe pas"


        except Exception as e:
            return e

