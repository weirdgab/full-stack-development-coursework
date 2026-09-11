let frase = '',
	b = eval(prompt('Valor'));
switch (b % 2) {
	case 0:
		frase = 'O número é par';
		break;
	case 1:
		frase = 'O número é ímpar';
		break;
}
alert(frase);
