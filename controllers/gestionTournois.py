from models.tournoi import Tournoi
import json,os,io
F = "data/tournaments/tournoi.json"

class GestionTournois:
    def __init__(self,id_tournoi , nom, lieu, date_debut,
                 date_fin ,description, tour_actuel = 0 ,nbr_tour = 4):
        self.id_tournoi = id_tournoi
        self.nom = nom
        self.lieu = lieu
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.nbr_tour = nbr_tour
        self.tour_actuel = tour_actuel
        self.description = description
    def ajouter_tournoi(self):
        """
        remplir les informations des tournois
        """
        id_tournoi = input("Entrer l'id  : ")
        nom = input("Entrer le nom : ")
        lieu = input("Entrer le lieu : ")
        date_debut = input("Entrer la date de debut : ")
        date_fin = input("Entrer la date de fin : ")
        nbr_tour = input("entrer le nombre de tour :")
        tour_actuel = input("entrer le tour actuel :")
        description = input("entrer la remarque :")
        print("Le tournoi N° ", id_tournoi, "son nom: ", nom,"de la tour N :",tour_actuel, "se pass au: ", lieu, "le : ",
              date_debut,"et se termine le :",date_fin,"ses remarques :",description,"nobmbre de tour :",nbr_tour)
        # retourner un objet de la classe Tournoi
        Tournois = {
            "id": id_tournoi,
            "nom": nom,
            "lieu": lieu,
            "date_debut": date_debut,
            "date_fin" : date_fin,
            "nbr_tour" : nbr_tour,
            "tour_actuel" : tour_actuel,
            "description" : description
            }
        data = []

        # check if file exist
        if os.path.isfile(F):
            # read and write in file
            with open(F, "r+") as jsonfile:
                try:
                    data = json.load(jsonfile)
                except:
                    json.dump(data, jsonfile)
        else:  # create json file
            with io.open(os.path.join(F), 'w') as jsonfile:
                jsonfile.write(json.dumps(data))

        new_data = Tournoi
        data.append(new_data)

        with open("data/tournaments/tournoi", "w") as jsonfile:
            json.dump(data, jsonfile)

    """
     afficher la liste des tournois
    """

def afficher_tournoi():
        fileObject = open("data/tournaments/tournoi.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)
        print(aList[0])
        fileObject.close()


"""
afficher le nom et la date d'une tournoi 
"""
def afficher_nom_date_tournoi():

    # Ouvrir le fichier JSON
    with open("data/tournaments/tournoi.json", "r") as file:
        tournois = json.load(file)

    # Tournoi donné en paramètre
    id_tournoi = 1

    # Rechercher le tournoi correspondant
    def recherche_tournoi(tournois, id_tournoi):
        for tournoi in tournois:
            if tournoi["id_tournoi"] == id_tournoi:
                return tournoi
        return None

    # Récupérer les informations pour le tournoi donné
    tournoi = recherche_tournoi(tournois, id_tournoi)
    if tournoi:
        nom_tournoi = tournoi["nom_tournoi"]
        date_debut_tournoi = tournoi["date_debut_tournoi"]
        print("Informations pour le tournoi '{}' :".format(id_tournoi))
        print("Nom :", nom_tournoi)
        print("Date :", date_debut_tournoi)
    else:
        print("Le tournoi '{}' n'a pas été trouvé.".format(id_tournoi))

afficher_nom_date_tournoi()




