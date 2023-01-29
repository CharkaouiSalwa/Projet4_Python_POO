from models.match import Match

class Tour:
    """
    la déclaraion des attributs d'instance
    """
    def __init__(self,id_tour, nom , date_heure_debut , date_heure_fin):
        self.id_tour = id_tour
        self.nom = nom
        self.date_heure_debut = date_heure_debut
        self.date_heure_fin = date_heure_fin
        self.match = Match.id_match

    #afficher le nom et le is match du tour
    def __str__(self):
        return self.nom + " : " + str(self.match)

    def start(self):
        self.date_heure_debut = True
        return True

    """
      avant de cloturer on demande si 
      tous les matchs sont finis
      et il n'existe plus de tuples
    """
    def close(self):
        for i in self.match:
            if type(i) != tuple:
                return False
            self.date_heure_fin = True
            return True




