class Puntos:

    def calcularResultado(self, set):
        for i in range(0, len(set)):
            if (i < 5):
                ronda = set[i]
                if ronda[0] == 1:
                    return "15-0"
                else:
                    return "0-0"

