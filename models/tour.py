from models.match import Match
import uuid
from datetime import datetime,date
class Tour:
    """
    la déclaraion des attributs d'instance
    """
    def __init__(self, nom_tour , date_heure_fin="", matchs=[]):
        # generate unique id
        id_tour = uuid.uuid4().int & (1 << 10) - 1
        self.id_tour = id_tour
        self.nom_tour = nom_tour
        # get dateNow
        db = datetime.today()
        date_heure_debut = db.strftime("%d/%m/%Y %H:%M:%S")
        self.date_heure_debut= date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.matchs = matchs



    def __str__(self):
        return self.id_tour + " : " + self.nom + " : " + self.date_heure_debut+ " : " + self.date_heure_fin










