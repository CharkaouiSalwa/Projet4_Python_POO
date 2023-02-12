from models.match import Match
import uuid
from datetime import datetime,date
class Tour:
    """
    la déclaraion des attributs d'instance
    """
    def __init__(self,nom_tournoi,id_tour, nom , date_heure_debut , date_heure_fin=""):
        # generate unique id
        id_tour = uuid.uuid4().int & (1 << 10) - 1
        # get dateNow
        db = datetime.today()
        date_heure_debut = db.strftime("%d/%m/%Y %H:%M:%S")
        self.nom_tournoi = nom_tournoi
        self.id_tour = id_tour
        self.nom = nom
        self.date_heure_fin = date_heure_fin
        self.match = Match.id_match


    def __str__(self):
        return self.id_tour + " : " + self.nom + " : " + self.date_heure_debut+ " : " + self.date_heure_fin


    def start(self):
        self.date_heure_debut = True
        return True






