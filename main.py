import json,os,io
import uuid
from datetime import datetime,date
import pathlib
from controllers.joueurController import joueurController
from controllers.tournoiController import tournoiController
from views.joueurView import JoueurView
from controllers.tourController import tourcontroller
from models.joueur import Joueur
#menu_principal()
def main():
 dossier = 'data/tournaments'
 #t = tournoiController()
 # print(t.afficher_tournois(dossier))
 #nom = 'saad'
 #t = tournoiController()
# t.add_tournoi('test2','lieu','01/01/2021','01/01/2022','remar')
 #print(t.get_nom_date_tournoi(nom))
 #nom_tournoi ='test'
 #v = JoueurView()
 #v = v.add_joueur(nom_tournoi)
 #v = joueurController()
 #v = joueurController()
 #print(v.get_joueurs_by_tournoi(nom_tournoi))
 #print(v.get_all_joueurs(dossier))
 #print (v.get_all_joueurs(dossier))
 #print (v.add_joueur("test2","azertr","eza","zeze","02/07/1994"))
 #print (v.add_joueur("test","salwas","salwd","test","02/07/1994"))
 #print (v.add_joueur("test","saadsa","saad","test","02/07/1994"))
 v = tourcontroller()
 v.add_tour('test','nassim')
 #print(v.close_tour('test2','saad'))
 #print(v.get_tours('test'))


if __name__ == "__main__":
    main()