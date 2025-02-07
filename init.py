att_type = ["magic", "physique", "ultime", "aucune", "détection", "production", "buff", "support"]
type_cible = ["air", "sol", "invisible", "hybride", "aucune", "allié", "bâtiment"]
effet = ["ralentissement", "aucune", "détecte les ennemis camouflés"]

class batiment:
    def __init__(self):
        self.att_type = ["magic", "physique", "ultime", "aucune", "détection", "production", "buff", "support"]
        self.type_cible = ["air", "sol", "invisible", "hybride", "aucune", "allié", "bâtiment"]
        self.effet = ["ralentissement", "aucune", "détecte les ennemis camouflés"]
        

    class Archer():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["hybride"]
            self.att_type = "physique"
            self.effet = "aucune"
            self.image = 0  # Remplacer avec le chemin de l'image
            self.degat = 5
            self.cooldown = 1000

    

    class PosteDeGuet():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["invisible"]
            self.att_type = "détection"
            self.effet = "détecte les ennemis camouflés"
            self.image = 0
            self.degat = 0
            self.cooldown = 0

    class CaserneDeRecrue():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["aucune"]
            self.att_type = "production"
            self.effet = "aucune"
            self.image = 0
            self.degat = 0
            self.cooldown = 0

    class TourDeGuet():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["allié"]
            self.att_type = "buff"
            self.effet = "aucune"
            self.image = 0
            self.degat = 0
            self.cooldown = 0

    class CampDeBucherons():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["bâtiment"]
            self.att_type = "support"
            self.effet = "aucune"
            self.image = 0
            self.degat = 0
            self.cooldown = 0

    class TourDeBaliste():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["hybride"]
            self.att_type = "physique"
            self.effet = "aucune"
            self.image = 0
            self.degat = 20
            self.cooldown = 3000

    class Moulin():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["aucune"]
            self.att_type = "production"
            self.effet = "aucune"
            self.image = 0
            self.degat = 0
            self.cooldown = 0

    class TourDeGarde():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["allié"]
            self.att_type = "buff"
            self.effet = "aucune"
            self.image = 0
            self.degat = 0
            self.cooldown = 0

    class MineDeFer():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["aucune"]
            self.att_type = "production"
            self.effet = "aucune"
            self.image = 0
            self.degat = 0
            self.cooldown = 0

    class TourDeMagie():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["hybride"]
            self.att_type = "magic"
            self.effet = "aucune"
            self.image = 0
            self.degat = 15
            self.cooldown = 2000

    class TourALaser():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["hybride"]
            self.att_type = "ultime"
            self.effet = "aucune"
            self.image = 0
            self.degat = 25
            self.cooldown = 1000

    class CanonOrbital():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["hybride"]
            self.att_type = "ultime"
            self.effet = "aucune"
            self.image = 0
            self.degat = 50
            self.cooldown = 5000

class spells():
    def __init__(self):
        self.effect = ["aucune", "dégâts", "soin", "buff", "ralentissement", "détection", "camouflage"]

    class ZoneDeRalentissement():
        def __init__(self):
            self.type = 'batiment'
            self.cible = ["aucune"]
            self.att_type = "aucune"
            self.effet = "ralentissement"
            self.image = 0
            self.degat = 0
            self.cooldown = 0


class unités:
    def __init__(self):
        self.type_cible = ["air", "sol", "invisible", "hybride", "aucune", "allié", "bâtiment"]
        self.effet = ["ralentissement", "aucune", "détecte les ennemis camouflés"]
        self.att_type = ["magic", "physique", "ultime", "aucune", "détection", "production", "buff", "support"]
        