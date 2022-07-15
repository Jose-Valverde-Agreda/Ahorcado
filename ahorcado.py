from palabras import palabras
import random
import string
from ahorcado_diagrama import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    # Seleccionar una palabra al azar de la lista de palabras válidas
    palabra = random.choice(palabras)
    # por si la palabra tiene algún guión o espacio
    while '-' in palabra or ' ' in palabra:
        # Seleccionamos otra palabra
        palabra = random.choice(palabras)
    return palabra.upper()

def ahorcado():
    print("========================================")
    print("   ¡Bienvendido al Juego del Ahorcado!  ")
    print("========================================")

    palabra = obtener_palabra_valida(palabras)

    letras_por_adivinar = set(palabra)
    letras_elegidas =  set()
    abecedario = set(string.ascii_uppercase) # No contiene la ñ

    vidas = 7

    while len(letras_por_adivinar) > 0 and vidas > 0:
        print(f"Te quedan {vidas} vida(s) y has usado estas letras : {' '.join(letras_elegidas)}")

        # Mostrar el estado actual de la palabra
        # USaremos list comprehension y if en modo short hand
        palabra_lista = [letra if letra in letras_elegidas else '-' for letra in palabra]
        # Mostramos estado del ahorcado
        print(vidas_diccionario_visual[vidas])
        # Mostramos estado actual de la palabra
        print(f"Palabra: {' '.join(palabra_lista)}")

        letra_usuario = input("Escoge una letra: ").upper()
        if letra_usuario in abecedario - letras_elegidas:
            letras_elegidas.add(letra_usuario)
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print('')
            else:
                vidas = vidas - 1
                print(f"\nTu letra, {letra_usuario} no está en la palabra.")
        elif letra_usuario in letras_elegidas:
            print("\nYa escogiste esa letra. Por favor escoge una nueva")
        else:
            print("\nEsta letra no es válida")
    # Nos quedamos sin letras por adivinar o sin vidas
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"Ahorcado!. Perdiste. Lo siento mucho. La palabra era : {palabra}")
    else:
        print(f"¡Excelente! ¡Adivinaste la palabra {palabra}!")


ahorcado()