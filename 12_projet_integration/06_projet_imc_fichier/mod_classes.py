class Patient:#Classe entité ou domaine
    def __init__(self, nom:str, age:int, poids:float, taille:float):
        self.nom = nom
        self.age = age
        self.poids = poids
        self.taille = taille

    def __str__(self):
        return "Nom:{}, age:{}, poids:{}, taille:{}".format(self.nom,
                                self.age, self.poids, self.taille)

    def calculer_imc(self):
        return self.poids / self.taille ** 2