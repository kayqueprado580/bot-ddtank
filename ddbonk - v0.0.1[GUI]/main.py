import tkinter as tk
from tkinter import ttk

def toggle_button(button, on_function=None):
    global active_button
    if active_button and active_button != button:
        clear_buttons()
    button_text = button["text"]
    if "OFF" in button_text:
        button["text"] = button_text.replace("OFF", "ON")
        button["bg"] = '#006400'
        active_button = button
        if on_function:
            on_function()
    else:
        button["text"] = button_text.replace("ON", "OFF")
        button["bg"] = '#8B0000' 
        active_button = None
        
    # Adicionando uma mensagem à console
    console_text.config(state=tk.NORMAL)
    console_text.insert(tk.END, f"{button['text']} clicado\n")
    # console_text.insert(tk.END, (f"{button['cget('text')']} desligado\n")))
    console_text.see(tk.END)  # Rolando para o final da console
    console_text.config(state=tk.DISABLED)
        
def clear_buttons():
    global active_button
    if active_button:
        active_button["text"] = active_button["text"].replace("ON", "OFF")
        active_button["bg"] = '#8B0000'
        active_button = None

def on_pvp():
    console_text.config(state=tk.NORMAL)
    console_text.insert(tk.END, "PVP ligado!\n")
    console_text.see(tk.END)
    console_text.config(state=tk.DISABLED)

def on_gvg():
    console_text.config(state=tk.NORMAL)
    console_text.insert(tk.END, "GVG ligado!\n")
    console_text.see(tk.END)
    console_text.config(state=tk.DISABLED)

def on_formigueiro():
    console_text.config(state=tk.NORMAL)
    console_text.insert(tk.END, "Formigueiro ligado!\n")
    console_text.see(tk.END)
    console_text.config(state=tk.DISABLED)

def on_galinheiro():
    console_text.config(state=tk.NORMAL)
    console_text.insert(tk.END, "Galinheiro ligado!\n")
    console_text.see(tk.END)
    console_text.config(state=tk.DISABLED)
    
def on_clear_log():
    console_text.config(state=tk.NORMAL)
    console_text.delete("1.0", tk.END)
    console_text.config(state=tk.DISABLED)
    
def on_key_press(event):
    if event.keysym == "Escape":
        if any(button["text"].endswith("(ON)") for button in [pvp_button, gvg_button, formigueiro_button, galinheiro_button]):
            clear_buttons()
            on_kick_script()
        else:
            app.destroy()
            
def on_kick_script():
    console_text.config(state=tk.NORMAL)
    console_text.insert(tk.END, "Script encerrado...\n")
    console_text.see(tk.END)
    console_text.insert(tk.END, "Até a próxima!\n")
    console_text.see(tk.END)
    console_text.config(state=tk.DISABLED)

# Criar a janela principal
app = tk.Tk()
app.title("DDBonk - v0.0.1")
app.iconbitmap("public/img/dd-ico.ico")  # Substitua pelo caminho do seu ícone

# Configurar estilo com ttkthemes
style = ttk.Style()
style.theme_use('clam')  # Pode escolher um tema diferente, 'clam' é um exemplo

# Estilo Dark
app.configure(bg='#1E1E1E')  # Cor de fundo escura

# Definir fontes e tamanhos
font_title = ("Helvetica", 18, "bold")
font_subtitle = ("Helvetica", 14, "underline")
font_button = ("Helvetica", 12)

title_label = tk.Label(app, text="DDBonk", font=font_title, bg='#1E1E1E', fg='#FFFFFF')  # Cor branca para o texto
title_label.pack(pady=10)

subtitle1_label = tk.Label(app, text="Salão de Jogos", font=font_subtitle, bg='#1E1E1E', fg='#FFFFFF')
subtitle1_label.pack(pady=5)

container1 = tk.Frame(app, bg='#1E1E1E', bd=2, relief=tk.GROOVE, pady=15)  # Adicionando borda branca ao redor do container
container1.pack(pady=10)

pvp_button = tk.Button(container1, text="PVP (OFF)", bg='#8B0000', fg='#FFFFFF', font=font_button, command=lambda: toggle_button(pvp_button, on_pvp))
gvg_button = tk.Button(container1, text="GVG (OFF)", bg='#8B0000', fg='#FFFFFF', font=font_button, command=lambda: toggle_button(gvg_button, on_gvg))

pvp_button.pack(side=tk.LEFT, padx=10)
gvg_button.pack(side=tk.LEFT, padx=10)

subtitle2_label = tk.Label(app, text="Central de Expedições", font=font_subtitle, bg='#1E1E1E', fg='#FFFFFF')
subtitle2_label.pack(pady=5)

container2 = tk.Frame(app, bg='#1E1E1E', bd=2, relief=tk.GROOVE, pady=15)  # Adicionando borda branca ao redor do container
container2.pack(pady=10)

formigueiro_button = tk.Button(container2, text="Formigueiro (OFF)", bg='#8B0000', fg='#FFFFFF', font=font_button, command=lambda: toggle_button(formigueiro_button, on_formigueiro))
galinheiro_button = tk.Button(container2, text="Galinheiro (OFF)", bg='#8B0000', fg='#FFFFFF', font=font_button, command=lambda: toggle_button(galinheiro_button, on_galinheiro))
formigueiro_button.pack(side=tk.LEFT, padx=10)
galinheiro_button.pack(side=tk.LEFT, padx=10)

# Console
console_label = tk.Label(app, text="Log", font=font_subtitle, bg='#1E1E1E', fg='#FFFFFF')
console_label.pack(pady=5)
console_frame = tk.Frame(app, bg='#1E1E1E', bd=2, relief=tk.GROOVE, pady=15)
console_frame.pack(pady=10)
console_clear_button = tk.Button(console_frame, text="Limpar", bg='#1E1E1E', fg='#F6F6F6', font=font_button, command=on_clear_log)
console_clear_button.pack(side=(tk.TOP), fill="x", expand=False, padx=10)

console_text = tk.Text(console_frame, bg='#1E1E1E', fg='#FFFFFF', wrap="word", state=tk.DISABLED)
console_text.pack(expand=True, fill="both", padx=10, pady=5)

# Configurações adicionais
app.geometry("375x675")  # Tamanho inicial
app.resizable(False, False)  # Impedir redimensionamento

# Configurar evento de teclado
app.bind("<KeyPress>", on_key_press)

# Variável global para rastrear o botão ativo
active_button = None

# Iniciar o loop de eventos
app.mainloop()
