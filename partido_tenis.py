class Puntos:

    def calcularResultado(self, set):
        if sum(set) == 0:
            return "0-0"
        if sum(set) == 1:
            return "15-0"