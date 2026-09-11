from tkinter import Tk, Button, Entry, messagebox


def saudacao():
    mensagem = texto.get()
    messagebox.showinfo('Saudação', mensagem)


janela = Tk()
texto = Entry(janela)
texto.pack()
botao = Button(janela, text="Olá", command=saudacao)
botao.pack()
janela.mainloop()
