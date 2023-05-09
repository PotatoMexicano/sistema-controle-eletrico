import threading
import tkinter as tk

from motor import Motor

motor = Motor()

thread_motor = threading.Thread(target=motor.inicia_motor, args=(True,))
thread_motor.daemon = True
thread_motor.start()

def update_value():
    # Função para atualizar o valor
    # Aqui você pode implementar a lógica desejada para atualizar o valor

    # Exemplo: Atualizar o valor somando 1
    global value
    value = motor.rotacoes
    value_label.config(text=str(f'{value:0.2f} RPM'))

    # Chama a função novamente após 100ms
    value_label.after(70, update_value)

def slider_callback(value):
    # Função de callback do slider
    # Exibe o valor selecionado pelo slider
    motor.amperes = int(value)

# Cria a janela principal
window = tk.Tk()
window.title("Atualização de Valor")

# Valor inicial
value = 0

# Cria o rótulo para exibir o valor
value_label = tk.Label(window, text=str(value), font=("Arial", 24), height=5, width=20)
value_label.pack(pady=20)

# Slider
slider = tk.Scale(window, from_=motor.amperes, to=100, orient=tk.HORIZONTAL, command=slider_callback)
slider.pack(pady=10)

# Botão "Desligar"
desligar_button = tk.Button(window, text="Desligar", command=motor.desliga_motor)
desligar_button.pack(pady=10)

# Chama a função de atualização inicialmente
update_value()

# Inicia o loop principal da janela
window.mainloop()
