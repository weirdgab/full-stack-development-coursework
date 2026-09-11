from tkinter import Tk, Label, Entry, Button

janela = Tk()

etiqueta = Label(janela, text='Nome:')
etiqueta.grid(row=0, column=1)

botao = Button(janela, text='Enviar')
botao.grid(row=0, column=2)

janela.mainloop()
