import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class ExemploSimples(BaseWidget):

    def __init__(self):
        super(ExemploSimples, self).__init__('ExemploSimples')
        self._nome = ControlText('Nome', 'Default value')
        self._sobrename = ControlText('Sobrenome')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Pressione o Botão')


if __name__ == '__main__':
    from pyforms import start_app
    start_app(ExemploSimples)
