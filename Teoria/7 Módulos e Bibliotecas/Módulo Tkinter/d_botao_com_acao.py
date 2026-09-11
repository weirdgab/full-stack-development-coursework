from tkinter import Tk, Button

def acao():
    print('Botão pressionado')

principal = Tk()

botao = Button(principal, text='Clique aqui', command=acao)
botao.place(x=100, y=25)

principal.mainloop()