import json
from models.tournoi import Tournoi
from views.menuView import menu_options
from views.menuView import menu_principal
import json,os,io
from views.tournoiView import tournoiView


def main():
   v = tournoiView()
   v.ajoutertournoi()
   #menu_principal()



if __name__ == "__main__":
    main()