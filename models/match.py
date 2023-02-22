import uuid


class Match:
    """
    déclaration des attributs d'instance
    """
    def __init__(self, id_national_1, score_J1, id_national_2, score_J2):
        id_match = uuid.uuid4().int & (1 << 10) - 1
        self.id_match = id_match
        self.id_national_1 = id_national_1
        self.score_J1 = score_J1
        self.id_national_2 = id_national_2
        self.score_J2 = score_J2
