// Função pura sempre retorna o mesmo resultado para as mesmas entradas:
function produto(a, b) {
	return a * b;
}

// Função impura altera a própria entrada na qual o valor poder variar:
let c = 5;
function soma(a) {
	return a + c;
}
