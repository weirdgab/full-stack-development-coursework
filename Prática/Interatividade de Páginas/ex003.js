const situacao = (valor_imc) => {
	if (valor_imc < 18.5) return 'Abaixo do peso.';
	else if (valor_imc < 25) return 'Peso ideal (parabéns).';
	else if (valor_imc < 30) return 'Levemente acima do peso.';
	else if (valor_imc < 35) return 'Obesidade de grau I.';
	else if (valor_imc < 40) return 'Obesidade grau II (servera).';
	else return 'Obesidade grau III (mórbida).';
};
