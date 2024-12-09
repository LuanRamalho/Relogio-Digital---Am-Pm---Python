import tkinter as tk
from tkinter import font
from datetime import datetime

# Variável para alternar entre os formatos de 24 horas e AM/PM
is_24_hour_format = True

def update_clock():
    """Atualiza o relógio na interface gráfica."""
    global is_24_hour_format
    now = datetime.now()
    hours = now.hour
    minutes = now.minute
    seconds = now.second

    if is_24_hour_format:
        time_string = f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        period = "AM" if hours < 12 else "PM"
        hours = hours % 12 or 12  # Converte para formato de 12 horas
        time_string = f"{hours:02}:{minutes:02}:{seconds:02} {period}"

    clock_label.config(text=time_string)
    clock_label.after(1000, update_clock)

def toggle_format():
    """Alterna entre os formatos de 24 horas e AM/PM."""
    global is_24_hour_format
    is_24_hour_format = not is_24_hour_format
    switcher_button.config(
        text="Formato AM/PM" if is_24_hour_format else "Formato 24 Horas"
    )

# Configuração da janela principal
root = tk.Tk()
root.title("Relógio Digital")
root.geometry("400x300")
root.configure(bg="#20d972")

# Estilo e fonte do relógio
clock_font = font.Font(family="Roboto Mono", size=40, weight="bold")
button_font = font.Font(family="Roboto Mono", size=14)

# Rótulo para exibir o relógio
clock_label = tk.Label(
    root, text="00:00:00", font=clock_font, bg="#0d0d0d", fg="white",
    padx=20, pady=20, relief="ridge", borderwidth=5
)
clock_label.pack(pady=30)

# Botão para alternar o formato do relógio
switcher_button = tk.Button(
    root, text="Formato AM/PM", font=button_font, bg="white", fg="#0d0d0d",
    padx=10, pady=5, relief="raised", borderwidth=3, command=toggle_format
)
switcher_button.pack()

# Inicia a atualização do relógio
update_clock()

# Inicia o loop da interface gráfica
root.mainloop()
