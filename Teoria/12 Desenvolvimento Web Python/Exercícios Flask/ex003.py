# Implementar uma solução em Python com Flask que faça:
# a. Exiba a mensagem: "Olá, programadores!" no endereço raiz de uma página web e apareça a mensagem "Entre com dois números".
# b. Exiba a mensagem: "0.0" no endereço "/somar/"
# c. Exiba a mensagem: "30.0" no endereço "/somar/10/20" de uma página web

from flask import Flask

app = Flask(__name__)


@app.route('/')
def cumprimento():
    boas_vindas = 'Olá, programadores!'
    numeros = 'Entre com dois números na url "somar".'
    return boas_vindas + numeros


@app.route('/somar/')
def somar():
    return '0.0'


@app.route('/somar/<n1>/<n2>')
def somando(n1, n2):
    n1 = int(n1)
    n2 = int(n2)
    resultado = n1 + n2
    resultadoString = str(resultado)
    return resultadoString


if __name__ == '__main__':
    app.run(debug=True)
