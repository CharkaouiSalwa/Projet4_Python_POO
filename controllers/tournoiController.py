from models.tournoi import Tournoi
import json
import os
import io
from datetime import datetime
PATH = "data/tournaments/"


class TournoiController:
    def __init__(self):
        self

    def validate(date_text):
        """Function to validate date with format jj/mm/aaaa"""
        try:
            if date_text != datetime.strptime(date_text, "%d/%m/%Y").strftime("%d/%m/%Y"):
                raise ValueError
            return True
        except ValueError:
            return False

    def add_tournoi(self, nom, lieu, date_debut, remarque, nbr_tour):
        """Ajouter un tournoi"""
        try:
            if len(str(nom)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            if len(str(lieu)) < 3:
                return "Le lieu du tournoi doit contenir au minimum trois caractères."
            if len(str(date_debut)) != 10 or not TournoiController.validate(date_debut):
                return "La date de debut du tournoi doit avoir le format jj/mm/aaaa."
            if len(str(remarque)) < 3:
                return "la remarque du tournoi doit contenir au minimum trois caractères."
            if int(nbr_tour) < 1:
                return "Le nombre de tour doit être supérieur à 0."
            tournois = Tournoi(nom, lieu, date_debut, remarque, nbr_tour)
            data = []
            F = PATH+"{}.json".format(nom)
            if os.path.isfile(F):
                with open(F, "r+") as jsonfile:
                    try:
                        data = json.load(jsonfile)
                        if data[0]["nom_tournoi"] == nom:
                            return 'Ce tournoi existe déja'
                    except ValueError:
                        json.dump(data, jsonfile)
            else:
                with io.open(os.path.join(F), 'w') as jsonfile:
                    jsonfile.write(json.dumps(data, indent=4))
            new_data = tournois.__dict__
            data.append(new_data)
            with open(F, "w") as jsonfile:
                json.dump(data, jsonfile)
            return "Le tournoi a été ajouté avec succès"
        except Exception as e:
            return e

    def get_tournois(self, dossier):
        """ Retourner tous les tournois"""
        try:
            listtournoi = []
            for fichier in os.listdir(dossier):
                if fichier.endswith(".json"):
                    path = os.path.join(dossier, fichier)
                    with open(path) as f:
                        data = json.load(f)
                        listtournoi.extend(data)
            return listtournoi
        except Exception as e:
            return e

    def get_nom_date_tournoi(self, nom):
        """Retourner le nom et la date du tournoi"""
        try:
            if len(str(nom)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            new_data = []
            a = PATH + nom + '.json'
            with open(a, 'r')as f:
                data = json.load(f)
            new_data.append(data[0]['nom_tournoi'])
            new_data.append(data[0]['date_debut'])
            new_data.append(data[0]['date_fin'])
            return new_data
        except Exception as e:
            return e

    def get_tournoi(self, nom):
        """Retourner un tournoi """
        try:
            if len(str(nom)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            a = PATH + nom + '.json'
            with open(a, 'r') as f:
                data = json.load(f)
            return data
        except Exception as e:
            return e
