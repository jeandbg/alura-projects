import tkinter as tk

janela = tk.Tk()
janela.title("Exemplo tkinter")
janela.geometry("300x200")

def clique():
    rotulo.config(text='voce clicou', font=("Courier New", 20))

rotulo = tk.Label(janela, text="Olá, Bem vindo", font=("Arial",12))
rotulo.pack(pady=1)

botao = tk.Button(janela, text="Clique aqui", command=clique)
botao.pack(pady=10)


janela.mainloop()