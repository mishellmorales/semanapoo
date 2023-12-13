# Programación Orientada a Objetos (POO)

class ClimaDiarioViento:
    def __init__(self):
        self.velocidades = []

    def ingresar_velocidades_diarias(self):
        for i in range(7):
            velocidad = float(input(f"Ingrese la velocidad del viento para el día {i + 1}: "))
            self.velocidades.append(velocidad)

    def calcular_promedio_semanal(self):
        promedio = sum(self.velocidades) / len(self.velocidades)
        return promedio

def main():
    clima_viento = ClimaDiarioViento()
    clima_viento.ingresar_velocidades_diarias()
    promedio_semanal = clima_viento.calcular_promedio_semanal()
    print(f"El promedio semanal de velocidades del viento es: {promedio_semanal:.2f}")

if __name__ == "__main__":
    main()
