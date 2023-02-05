from models.tournoi import Tournoi
import json,os,io
from datetime import datetime


class tournoiController:
    def __init__(self,tournois):
        self.tournois = tournois

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
    def ajouter_tournoi(self,nom,lieu,date_debut,date_fin,description):
        Tournois = Tournoi( nom, lieu, date_debut, date_fin, description)
        data = []
        F = "data/tournaments/{}.json".format(nom)
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
"""
 afficher la liste des tournois
"""

# def afficher_tournoi():
#         fileObject = open("data/tournaments/tournoi.json", "r")
#         jsonContent = fileObject.read()
#         aList = json.loads(jsonContent)
#         print(aList[0])
#         fileObject.close()
#
#
# """
# afficher le nom et la date d'une tournoi
# """
# def afficher_nom_date_tournoi():
#
#     # Ouvrir le fichier JSON
#     with open("data/tournaments/tournoi.json", "r") as file:
#         tournois = json.load(file)
#
#     # Tournoi donné en paramètre
#     id_tournoi = 1
#
#     # Rechercher le tournoi correspondant
#     def recherche_tournoi(tournois, id_tournoi):
#         for tournoi in tournois:
#             if tournoi["id_tournoi"] == id_tournoi:
#                 return tournoi
#         return None
#
#     # Récupérer les informations pour le tournoi donné
#     tournoi = recherche_tournoi(tournois, id_tournoi)
#     if tournoi:
#         nom_tournoi = tournoi["nom_tournoi"]
#         date_debut_tournoi = tournoi["date_debut_tournoi"]
#         print("Informations pour le tournoi '{}' :".format(id_tournoi))
#         print("Nom :", nom_tournoi)
#         print("Date :", date_debut_tournoi)
#     else:
#         print("Le tournoi '{}' n'a pas été trouvé.".format(id_tournoi))
#




