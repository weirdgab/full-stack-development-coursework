from tkinter import Button, Entry, Label, Tk, messagebox

from b_modulo_imc import calcula_imc, classifica_imc


def calcular():
    indice = calcula_imc(float(peso.get()), float(altura.get()))
    classificacao = classifica_imc(indice)
    messagebox.showinfo("Resultado do IMC", classificacao)


janela = Tk()

Label(janela, text="Altura").grid(row=0, column=1)
altura = Entry(janela)
altura.grid(row=0, column=2)

Label(janela, text="Peso").grid(row=1, column=1)
peso = Entry(janela)
peso.grid(row=1, column=2)

Button(janela, text="Calcular", command=calcular).grid(row=2, column=2)

janela.mainloop()
