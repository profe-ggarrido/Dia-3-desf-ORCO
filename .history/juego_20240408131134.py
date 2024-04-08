from personaje import Personaje
import random

print("Bienvenido a Gran Fantasía")

nombre = input("Por favor, indique el nombre de su personaje: \n")
p = Personaje(nombre)

print("¡Oh no, ha aparecido un Orco!")

o = Personaje('Orco')

while True:
    opcion = int(input(
        f"""Con tu nivel actual, tienes {p.get_probabilidad_ganar(o)*100}% de probabilidades
        de ganarle al Orco.
        Si ganas, ganarás 50 puntos de experiencia y el Orco perderá 30.
        Si pierdes, perderás 30 puntos de experiencia y el Orco ganará 50.
        ¿Qué deseas hacer?
        1. Atacar
        2. Huir
        """
    ))

    if opcion == 1:  # Atacar
        if p.ganar_combate(o):
            print("¡Le has ganado al Orco, felicidades!")
            # Mostrar estado actual de los personajes
            print(f"Estado actual de {p.nombre}: Nivel {p.nivel}, Experiencia {p.experiencia}")
            print(f"Estado actual de {o.nombre}: Nivel {o.nivel}, Experiencia {o.experiencia}")
            break  # Salir del ciclo si el jugador gana
        else:
            print("¡Oh no! El Orco te ha ganado.")
            # Mostrar estado actual de los personajes
            print(f"Estado actual de {p.nombre}: Nivel {p.nivel}, Experiencia {p.experiencia}")
            print(f"Estado actual de {o.nombre}: Nivel {o.nivel}, Experiencia {o.experiencia}")
    elif opcion == 2:  # Huir
        print("¡Has huido! El Orco ha quedado atrás.")
        break  # Salir del ciclo si el jugador decide huir
    else:
        print("Opción inválida. Por favor, elige una opción válida.")
