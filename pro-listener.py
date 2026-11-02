import random
import time


def main():
    # Lista con las posibles respuestas
    answers = [
        "Tiene sentido.",
        "Es una preocupación válida.",
        "Eso parece frustrante.",
        "Eso parece un gran desafío.",
        "Eso parece abrumador.",
        "Eso suena difícil.",
        "Vaya, eso debe ser muy duro.",
        "¿A qué te refieres?",
        "¿Cuál es tu teoría de por qué ocurre eso?",
        "¿Qué más?",
        "Parece que tienes un motivo para decir eso.",
        "Eso debe ser complicado.",
        "Suena difícil.",
        "¿Cómo ha sido eso para ti?",
        "Cuéntame más sobre eso.",
        "Entiendo por qué te sientes de esa manera.",
        "Te escucho.",
        "¿Qué necesitas en este momento?",
        "Gracias por confiarme esto.",
        "Aprecio que compartas esto conmigo.",
    ]

    # Saludo inicial al usuario
    print("Hola, estoy aquí para escuchar todos tus problemas.")
    print("Puedes escribir 'salir' para cerrar el programa.")
    print("Por favor, escribe lo que quieras contarme.\n")

    # Abre el archivo para guardar la sesión ('a' para añadir al final)
    # Se especifica encoding="utf-8" para guardar tildes y caracteres especiales correctamente
    with open("log.txt", "a", encoding="utf-8") as file:
        while True:
            # Solicita la entrada del usuario
            user_input = input("Escribe aquí: ").strip()

            # Protocolo de salida (permite 'salir' o 'quit', sin importar mayúsculas)
            if user_input.lower() in ("salir", "quit"):
                break

            # Si el usuario presiona Enter sin escribir nada, continúa el ciclo
            if not user_input:
                continue

            # Elige una respuesta aleatoria
            r_answer = random.choice(answers)

            # Espera para simular el efecto de "pensar"
            time.sleep(2)

            # Muestra la respuesta
            print(f"{r_answer}\n")

            # Guarda la conversación en el archivo
            file.write(f"Usuario: {user_input}\n")
            file.write(f"Bot:     {r_answer}\n")
            file.write("------------------------\n")

            # Vacía el búfer para asegurarse de que se guarde de inmediato
            file.flush()

    print("\nSesión guardada. ¡Hasta luego!")


if __name__ == "__main__":
    main()
