from models.joueur import Joueur
from controllers.gestionTournois import GestionTournois
import json,os,io
PATH = "data/tournaments/tournoi.json"

class GestionJoueurs:
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

        Joueur = { #retourner un objet de la classe joueur
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

        with open("data/data/tournaments/tournoi.json", "w") as jsonfile:
            json.dump(data, jsonfile)

    """
       afficher tous des joueurs
       """
def afficher_joueur():

     fileObject = open("data/tournaments/tournoi.json", "r")
     jsonContent = fileObject.read()
     aList = json.loads(jsonContent)
     print(aList[0]['joueurs'])
     fileObject.close()

afficher_joueur()

"""
afficher les joueurs par tournoi donnée en parametre
"""

def afficher_joueur_tournoi():

    # Ouvrir le fichier JSON
    with open("data/tournaments/tournoi.json", "r") as file:
        tournois = json.load(file)

    # Tournoi donné en paramètre
    nom_tournoi = "Paris 1"

    # Rechercher le tournoi correspondant
    def recherche_tournoi(tournois, nom):
        for tournoi in tournois:
            if tournoi["nom_tournoi"] == nom:
                return tournoi
        return None

    # Récupérer la liste de joueurs pour le tournoi donné
    tournoi = recherche_tournoi(tournois, nom_tournoi)
    if tournoi:
        joueurs = tournoi["joueurs"]
        print("Liste des joueurs pour le tournoi '{}':".format(nom_tournoi))
        for joueur in joueurs:
            print(joueur)
    else:
        print("Le tournoi '{}' n'a pas été trouvé.".format(nom_tournoi))

afficher_joueur_tournoi()





