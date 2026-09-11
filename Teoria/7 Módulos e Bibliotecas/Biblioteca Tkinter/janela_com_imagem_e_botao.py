from tkinter import *

def funcClicar():
    print("Botão pressionado")

janelaPrincipal = Tk()
texto = Label(master = janelaPrincipal, text = "Minha janela exibida")
texto.pack

pic = PhotoImage(file="/home/weirdgab/Scripts/Faculdade/Python/Conteúdo/7 Módulos e Bibliotecas/Biblioteca Tkinter/I _LOVE_HIMMMMM.jpeg")
logo = Label(master = janelaPrincipal, image = pic)
logo.pack

botao = Button (master = janelaPrincipal, text = 'Clique', command = funcClicar)
botao.pack()

janelaPrincipal.mainloop()