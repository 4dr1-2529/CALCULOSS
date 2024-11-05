import math

class CalculosEstadisticos:
    def calcular_media(self, num):

        if not num:
            return None
        return sum(num) / len(num)

    def calcular_desviacion_estandar(self, num):

        if not num:
            return None
        media = self.calcular_media(num)

        varianza = sum((x - media) ** 2 for x in num) / (len(num) - 1)
        return math.sqrt(varianza)
