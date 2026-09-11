# Implementar uma solução em Python com Flask que faça:
# a. Exiba a mensagem: "Página principal" no endereçp raiz de uma página web;
# b. Exiba a mensagem: "Olá, mundo!" no endereço "/ola/" de uma página web;
# c. Exiba a mensagem: "Olá, "nome"!" no endereço "/ola/"nome"" de uma página web

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Página principal'


@app.route('/ola/')
@app.route('/ola/<nome>')
def ola_mundo(nome='mundo'):
    return 'Olá, ' + nome + '!'


if __name__ == '__main__':
    app.run()
