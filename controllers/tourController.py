import json,os,io
PATH = "data/tour.json"

# class tourController:
#     def __init__(self,Tours):
#         self.tours = Tours
#
#
#     def ajouter_tour(self):
#         """
#         remplir les informations des tours
#         """
#         id_tour = input("Entrer l'id du tour : ")
#         nom = input("Entrer le nom : ")
#         date_heure_debut = input("Entrer la date et l'heure de debut : ")
#         date_heure_fin = input("Entrer la date et l'heure de fin : ")
#         print("Le tour N° ", id_tour, "son nom: ", nom, "la date et l'heure du debit: ", date_heure_debut, "la date et heure de fin : ",
#               date_heure_fin)
#
#         Tour = { #retourner un objet de la classe tour
#             "id": id_tour,
#             "nom": nom,
#             "date_heure_debut": date_heure_debut,
#             "date_heure_fin": date_heure_fin}
#         data = []
#
#         # check if file exist
#         if os.path.isfile(PATH):
#             # read and write in file
#             with open(PATH, "r+") as jsonfile:
#                 try:
#                     data = json.load(jsonfile)
#                 except:
#                     json.dump(data, jsonfile)
#         else:  # create json file
#             with io.open(os.path.join(PATH), 'w') as jsonfile:
#                 jsonfile.write(json.dumps(data))
#
#         new_data = Tour
#         data.append(new_data)
#
#         with open("data/tour.json", "w") as jsonfile:
#             json.dump(data, jsonfile)
#
#
