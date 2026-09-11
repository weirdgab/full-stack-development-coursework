from sklearn.datasets import load_digits
digitos = load_digits()

# Existem 1797 imagens, sendo que cada uma tem uma dimensão 8 x 8 = 64
print('Shape dos dados de imagens:{}'.format(digitos.data.shape))
print('Shape dos dados rotulados: {}'.format(digitos.target.shape))
