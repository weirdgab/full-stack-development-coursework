# Implementar uma solução em Python com Flask que faça:
# a. Exiba a mensagem: "Olá, programadores!" no endereço raiz de uma página web e apareça o link "/user/Usuário"
# b. Exiba a mensagem: "Olá, Usuário!" no endereço "/user/" e exiba a mensagem "Altere o endereços do browser e recarregue a página"
# c. Exiba a mensagem: "Olá, nome_usuário!" no endereço "/user/nome_do_usuário" de uma página web

from flask import Flask

app = Flask(__name__)


@app.route('/user/Usuário')
def ola_p():
    return 'Olá, programadores!'


@app.route('/user/<nome>')
def user(nome='usuário'):
    return 'Olá, ' + nome
