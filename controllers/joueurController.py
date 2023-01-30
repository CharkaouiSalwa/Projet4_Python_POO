from models.joueur import Joueur
import json,os,io
PATH = "data/datafile.json"

class JoueurController:
    def __init__(self,joueurs):
        self.joueurs = joueurs

    def ajouter_joueur(self):
        """
        remplir les informations des joueurs
        """
        id_national = input("Entrer l'id national du joueur : ")
        nom = input("Entrer le nom : ")
        prenom = input("Entrer le prénom : ")
        date_naissance = input("Entrer la date de naissance : ")
        print("Le Joueur N° ", id_national, "son nom: ", nom, "son prénom: ", prenom, "sa date de naissance : ",
              date_naissance)

        Joueur = {
            "id_national": id_national,
            "nom": nom,
            "prenom": prenom,
            "date_naissance": date_naissance}
        data = []

        # check if file exist
        if os.path.isfile(PATH):
            # read and write in file
            with open(PATH, "r+") as jsonfile:
                try:
                    data = json.load(jsonfile)
                except:
                    json.dump(data, jsonfile)
        else:  # create json file
            with io.open(os.path.join(PATH), 'w') as jsonfile:
                jsonfile.write(json.dumps(data))

        new_data = Joueur
        data.append(new_data)

        with open("data/joueurs.json", "w") as jsonfile:
            json.dump(data, jsonfile)
