from models.tournoi import Tournoi
import json,os,io
from datetime import datetime
PATH = "data/tournaments/"

class tournoiController:
    def __init__(self):
        self

    """
    Function to validate date with format jj/mm/aaaa
    """
    def validate(date_text):
        try:
            #strftime("%d/%m/%Y")
            if date_text != datetime.strptime(date_text, "%d/%m/%Y").strftime("%d/%m/%Y"):
                raise ValueError
            return True
        except Exception as e :
            return False
    def add_tournoi(self,nom,lieu,date_debut,date_fin,remarque):
        try:
            if len(str(nom)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(lieu)) < 3:
                return "Le lieu du tournoi doit contenir au minimum trois caractères."
            if len(str(date_debut)) != 10 and tournoiController.validate(date_debut) == False:
                return "La date de debut du tournoi doit avoir le format jj/mm/aaaa."
            if len(str(date_fin)) != 10 and tournoiController.validate(date_fin) == False:
                return "La date de fin du tournoi doit avoir le format jj/mm/aaaa."
            elif date_fin < date_debut:
                return "La date de fin du tournoi doit etre superieur ou égal à la date de debut."
            if len(str(remarque)) < 3:
                return "la remarque du tournoi doit contenir au minimum trois caractères."
            Tournois = Tournoi( nom, lieu, date_debut, date_fin, remarque)
            data = []
            F = PATH+"{}.json".format(nom)
            # check if file exist
            if os.path.isfile(F):
                # read and write in file
                with open(F, "r+") as jsonfile:
                    try:
                        data = json.load(jsonfile)
                        if data[0]["nom"] == nom:
                            return 'ce tournoi existe déja'
                    except:
                        json.dump(data, jsonfile)
            else:  # create json file
                with io.open(os.path.join(F), 'w') as jsonfile:
                    jsonfile.write(json.dumps(data))

            new_data = Tournois.__dict__
            data.append(new_data)
            with open(F, "w") as jsonfile:
                data[0]['joueurs'] = []
                data[0]['tours'] = []
                json.dump(data, jsonfile)
            return data
        except Exception as e :
            return e

    def get_tournois(self,dossier):
        try:
            listtournoi = []
            for fichier in os.listdir(dossier):
                if fichier.endswith(".json"):
                    path = os.path.join(dossier, fichier)
                    with open(path) as f:
                        data = json.load(f)
                        listtournoi.append(data)

            return listtournoi
        except Exception as e :
            return e

    def get_nom_date_tournoi(self, nom):
        try :
            if len(str(nom)) < 3 :
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            new_data = []
            a = PATH + nom + '.json'
            with open(a,'r')as f:
                data = json.load(f)
            new_data.append(data[0]['nom'])
            new_data.append(data[0]['date_debut'])
            new_data.append(data[0]['date_fin'])
            return new_data
        except Exception as e :
            return e












