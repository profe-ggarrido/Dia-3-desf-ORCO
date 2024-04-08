from personaje import Personaje
import random

print("Bienvenido a Gran Fantasía")

nombre = input("Por favor, indique el nombre de su personaje: \n")
p = Personaje(nombre)

print("¡Oh no, ha aparecido un Orco!")

o = Personaje('Orco')

while True:
    print("Selecciona una acción:")
    print("1. Atacar")
    print("2. Huir")

    opcion = int(input())

    if opcion == 1:  # Atacar
        if p.ganar_combate(o):
            print("¡Le has ganado al Orco, felicidades!")
        else:
            print("¡Oh no! El Orco te ha ganado.")
        
        # Mostrar estado actual de los personajes
        print(f"Estado actual de {p.nombre}: Nivel {p.nivel}, Experiencia {p.experiencia}")
        print(f"Estado actual de {o.nombre}: Nivel {o.nivel}, Experiencia {o.experiencia}")
    elif opcion == 2:  # Huir
        print("¡Has huido! El Orco ha quedado atrás.")
        break
    else:
        print("Opción inválida. Por favor, elige una opción válida.")
