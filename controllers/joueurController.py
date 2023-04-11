from models.joueur import Joueur
from controllers.tournoiController import TournoiController
import json
import os
PATH = "data/tournaments/"


class JoueurController:

    def __init__(self):
        self

    def add_joueur(self, nom_tournoi, id_national, nom, prenom, date_naissance):
        """Ajouter un joueur"""
        try:
            if len(str(id_national)) != 6:
                return "L'Id national est incorrect"
            if len(str(nom)) < 3:
                return "Le nom doit contenir au minimum trois caractères."
            if len(str(prenom)) < 3:
                return "Le prenom doit contenir au minimum trois caractères."
            if len(str(date_naissance)) != 10 or not TournoiController.validate(date_naissance):
                return "La date de naissance du joueur doit avoir le format jj/mm/aaaa."
            joueurs = Joueur(id_national, nom, prenom, date_naissance)
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                # read and write in file
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                    for joueur in data[0]['joueurs']:
                        if joueur["id_national"] == id_national:
                            return 'Un joueur avec cet id national existe déja'
                with open(a, 'w') as jsonfile:
                    new_data = joueurs.__dict__
                    data[0]["joueurs"].append(new_data)
                    json.dump(data, jsonfile)
                return "Le joueur a été ajouté avec succès"
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e:
            return e

    def get_joueurs_by_tournoi(self, nom_tournoi):
        """retourner tous les joueurs d'un tournoi"""
        try:
            if len(str(nom_tournoi)) < 3:
                return "Le nom du tournoi doit contenir au minimum trois caractères."
            a = PATH + nom_tournoi + '.json'
            # check if file exist
            if os.path.isfile(a):
                with open(a, "r") as jsonfile:
                    data = json.load(jsonfile)
                return data[0]['joueurs']
            else:
                return "Le nom de tournoi n'existe pas"
        except Exception as e:
            return e

    def get_all_joueurs(self, dossier):
        """retourner tous les joueurs de tous les tournois"""
        try:
            listtournoi = []
            for fichier in os.listdir(dossier):
                if fichier.endswith(".json"):
                    path = os.path.join(dossier, fichier)
                    with open(path) as f:
                        data = json.load(f)
                        listtournoi.extend(data[0]["joueurs"])
            return listtournoi
        except Exception as e:
            return e
