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
        except ValueError:
            return False
    def add_tournoi(self,nom,lieu,date_debut,date_fin,remarque):
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
            json.dump(data, jsonfile)
        return data

    def get_tournois(self,dossier):
        listtournoi = []
        for fichier in os.listdir(dossier):
            if fichier.endswith(".json"):
                path = os.path.join(dossier, fichier)
                with open(path) as f:
                    data = json.load(f)
                    listtournoi.append(data)

        return listtournoi

    def get_nom_date_tournoi(self, nom):
        new_data = []
        a = PATH + nom + '.json'
        with open(a,'r')as f:
            data = json.load(f)
        new_data.append(data[0]['nom'])
        new_data.append(data[0]['date_debut'])
        new_data.append(data[0]['date_fin'])

        return new_data












