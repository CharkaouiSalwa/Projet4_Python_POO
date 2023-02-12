from models.joueur import Joueur
from controllers.tournoiController import tournoiController
import uuid
import json,os,io
PATH = "data/tournaments/"


class joueurController:
    def __init__(self):
        self

    def add_joueur(self,nom_tournoi,id_national,nom,prenom,date_naissance):
        try:
            if len(str(id_national)) != 6:
                return "L'Id national est incorrect"
            if len(str(nom)) < 3 :
                return "Le nom doit contenir au minimum trois caractères."
            if len(str(prenom)) < 3 :
                return "Le prenom doit contenir au minimum trois caractères."
            if len(str(date_naissance)) != 10 and tournoiController.validate(date_naissance) == False:
                return "La date de naissance du joueur doit avoir le format jj/mm/aaaa."
            Joueurs = Joueur(id_national,nom, prenom,date_naissance)
            data = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                # read and write in file
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                with open(a,'w') as jsonfile:
                    new_data = Joueurs.__dict__
                    data[0]["joueurs"].append(new_data)
                    json.dump(data, jsonfile)

                return data
            else:
                return "Le nom de tournoi n'existe pas"
        except ValueError:
            return ValueError


    """
    retourner tous les joueurs d'un tournoi
    """
    def get_joueurs_by_tournoi(self,nom_tournoi):
        try :
            if len(str(nom_tournoi)) < 3 :
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            data = []
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                return (data[0]['joueurs'])
            else :
                return "Le nom de tournoi n'existe pas"
        except ValueError :
            return ValueError

    """
    retourner tous les joueurs de tous les tournois
    """
    def get_all_joueurs(self,dossier):
        try :
            listtournoi = []
            for fichier in os.listdir(dossier):
                if fichier.endswith(".json"):
                    path = os.path.join(dossier, fichier)
                    with open(path) as f:
                        data = json.load(f)
                        listtournoi.extend(data[0]["joueurs"])
                        #json.dump(listtournoi, f)
            return listtournoi
        except Exception as e:
            return e






