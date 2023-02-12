from models.tour import Tour
from controllers.tournoiController import tournoiController
import json,os
from datetime import datetime
PATH = "data/tournaments/"
class Tourcontroller :
    def __init__(self):
        self

    def add_tour(self,nom_tournoi,id_tour, nom , date_heure_debut , date_heure_fin):
        try:
            if len(str(id_tour)) != 6:
                return "L'Id tour est incorrect"
            if len(str(nom)) < 3 :
                return "Le nom doit contenir au minimum trois caractères."

            tours = Tour(nom_tournoi,id_tour, nom , date_heure_debut , date_heure_fin)
            data = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                # read and write in file
                with open(a, "r+") as jsonfile:
                    data = json.load(jsonfile)
                    if not data[0]["tours"]:

                        return 'tours existe'
                    else:
                        return "tours non existe"

            else:
                return "Le nom de tournoi n'existe pas"


        except Exception as e :
            return e

    """
        retourner tous les tours d'un tournoi
        """

    def get_tours(self, nom_tournoi):
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