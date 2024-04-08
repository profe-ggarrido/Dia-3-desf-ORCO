class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = 0

    def get_probabilidad_ganar(self, other):
        if self.nivel < other.nivel:
            return 0.33
        elif self.nivel > other.nivel:
            return 0.66
        else:
            return 0.5

    def ganar_combate(self, other):
        probabilidad_ganar = self.get_probabilidad_ganar(other)
        numero = random.uniform(0, 1)
        if numero < probabilidad_ganar:
            self.experiencia += 50
            other.experiencia -= 30
            return True
        else:
            self.experiencia -= 30
            other.experiencia += 50
            return False
