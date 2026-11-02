import random
import tkinter as tk
from tkinter import scrolledtext, ttk


class ListenerGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Pro Listener 2")
        self.root.geometry("520x620")
        self.root.minsize(420, 500)
        self.root.configure(bg="#f4f5f7")

        # Lista de respuestas 
        self.answers = [
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

        self._crear_interfaz()

    def _crear_interfaz(self):
        # --- Encabezado / Saludo ---
        header_frame = tk.Frame(self.root, bg="#2c3e50", padx=15, pady=12)
        header_frame.pack(fill=tk.X)

        title_lbl = tk.Label(
            header_frame,
            text="Estoy aquí para escucharte",
            font=("Segoe UI", 13, "bold"),
            fg="#ffffff",
            bg="#2c3e50",
        )
        title_lbl.pack(anchor="w")

        sub_lbl = tk.Label(
            header_frame,
            text="Escribe lo que sientes. La conversación se guarda automáticamente.",
            font=("Segoe UI", 9),
            fg="#bdc3c7",
            bg="#2c3e50",
        )
        sub_lbl.pack(anchor="w")

        # --- Área de Chat (Historial) ---
        self.chat_display = scrolledtext.ScrolledText(
            self.root,
            wrap=tk.WORD,
            font=("Segoe UI", 10),
            bg="#ffffff",
            fg="#2c3e50",
            relief=tk.FLAT,
            padx=12,
            pady=12,
        )
        self.chat_display.pack(
            fill=tk.BOTH, expand=True, padx=15, pady=(15, 5)
        )

        # Configuración de estilos visuales para los textos
        self.chat_display.tag_config(
            "user", foreground="#1a5276", font=("Segoe UI", 10, "bold")
        )
        self.chat_display.tag_config(
            "bot", foreground="#1e8449", font=("Segoe UI", 10, "bold")
        )
        self.chat_display.tag_config("text", foreground="#2c3e50")
        self.chat_display.tag_config(
            "system", foreground="#7f8c8d", font=("Segoe UI", 9, "italic")
        )
        self.chat_display.config(state=tk.DISABLED)

        # --- Etiqueta de estado ("Escribiendo...") ---
        self.status_lbl = tk.Label(
            self.root,
            text="",
            font=("Segoe UI", 9, "italic"),
            fg="#7f8c8d",
            bg="#f4f5f7",
        )
        self.status_lbl.pack(anchor="w", padx=18, pady=(0, 2))

        # --- Controles de Entrada (Input + Botón) ---
        input_frame = tk.Frame(self.root, bg="#f4f5f7", padx=15, pady=10)
        input_frame.pack(fill=tk.X)

        self.entry = ttk.Entry(input_frame, font=("Segoe UI", 10))
        self.entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 8))
        self.entry.focus()

        # Enviar mensaje con la tecla Enter
        self.entry.bind("<Return>", lambda event: self.enviar_mensaje())

        self.btn_send = tk.Button(
            input_frame,
            text="Enviar",
            font=("Segoe UI", 9, "bold"),
            bg="#3498db",
            fg="#ffffff",
            activebackground="#2980b9",
            activeforeground="#ffffff",
            relief=tk.FLAT,
            padx=15,
            pady=5,
            cursor="hand2",
            command=self.enviar_mensaje,
        )
        self.btn_send.pack(side=tk.RIGHT)

    def _agregar_texto(self, prefijo, texto, tag_prefijo):
        """Inserta texto en el área de chat de forma segura."""
        self.chat_display.config(state=tk.NORMAL)
        if prefijo:
            self.chat_display.insert(tk.END, f"{prefijo}: ", tag_prefijo)
        self.chat_display.insert(tk.END, f"{texto}\n\n", "text")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

    def _guardar_en_log(self, usuario, bot):
        """Registra la interacción en log.txt usando UTF-8."""
        with open("log.txt", "a", encoding="utf-8") as file:
            file.write(f"Usuario: {usuario}\n")
            file.write(f"Bot:     {bot}\n")
            file.write("------------------------\n")

    def enviar_mensaje(self):
        mensaje = self.entry.get().strip()
        if not mensaje:
            return

        # Si el usuario escribe 'salir' o 'quit', cerramos la ventana
        if mensaje.lower() in ("salir", "quit"):
            self.root.destroy()
            return

        # Muestra el mensaje del usuario y limpia la caja de texto
        self._agregar_texto("Tú", mensaje, "user")
        self.entry.delete(0, tk.END)

        # Desactiva la entrada temporalmente y muestra estado de espera
        self.entry.config(state=tk.DISABLED)
        self.btn_send.config(state=tk.DISABLED)
        self.status_lbl.config(text="El bot está respondiendo...")

        # Simula los 2 segundos de espera (2000 ms) sin bloquear la GUI
        self.root.after(2000, self._responder, mensaje)

    def _responder(self, mensaje_usuario):
        respuesta = random.choice(self.answers)
        self._agregar_texto("Bot", respuesta, "bot")

        # Guarda en archivo de registro
        self._guardar_en_log(mensaje_usuario, respuesta)

        # Restablece el estado de los controles
        self.status_lbl.config(text="")
        self.entry.config(state=tk.NORMAL)
        self.btn_send.config(state=tk.NORMAL)
        self.entry.focus()


if __name__ == "__main__":
    ventana = tk.Tk()
    app = ListenerGUI(ventana)
    ventana.mainloop()
