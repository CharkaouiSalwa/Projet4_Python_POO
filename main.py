import json
from models.tournoi import Tournoi
from views.menuView import menu_options
from views.menuView import menu_principal
import json,os,io
from views.tournoiView import tournoiView
from controllers.tournoiController import tournoiController
import uuid
from datetime import date
import pathlib

#menu_principal()
def main():
 # dossier = 'data/tournaments'
 t = tournoiController()
 #t.add_tournoi('test','lieu','dd','dd','remar')
 # print(t.afficher_tournois(dossier))
 #nom = 'saad'
 #t = tournoiController()
 #print(t.get_nom_date_tournoi(nom))


if __name__ == "__main__":
    main()