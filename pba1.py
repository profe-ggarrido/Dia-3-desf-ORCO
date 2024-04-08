from personaje import Personaje
import random

print("Bienvenido a Gran Fantasía")

nombre = input("Por favor, indica el nombre de tu personaje: \n")
p = Personaje(nombre)

print("¡Oh no, ha aparecido un Orco!")

o = Personaje('Orco')

while True:
    opcion = int(input(
        f"""Con tu nivel actual, tienes {p.get_probabilidad_ganar(o)*100}% de probabilidades
        de ganarle al Orco.
        Si ganas, ganarás 50 puntos de experiencia y el orco perderá 30.
        Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.
        ¿Qué deseas hacer?
        1. Atacar
        2. Defender
        3. Usar habilidad especial
        4. Huir
        """
    ))

    if opcion == 1:  # Atacar
        numero = random.uniform(0, 1)
        resultado = 'G' if numero < p.get_probabilidad_ganar(o) else 'P'
        if resultado == 'G':
            print("¡Le has ganado al orco, felicidades!")
            p.estado = 50
            o.estado = -30
        elif resultado == 'P':
            print("¡Oh no! El Orco te ha ganado.")
            p.estado = -30
            o.estado = 50
    elif opcion == 2:  # Defender
        # Implementa la lógica de defenderse
        pass
    elif opcion == 3:  # Usar habilidad especial
        # Implementa la lógica de habilidades especiales
        pass
    elif opcion == 4:  # Huir
        print("¡Has huido! El orco ha quedado atrás.")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")
