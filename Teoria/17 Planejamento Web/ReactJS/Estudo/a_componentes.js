// Representação de componentes com funções

function somaNums(A, B) {
	return A + B;
}

function prodNums(A, B) {
	return A * B;
}

function quadSomaNums(A, B) {
	return prodNums(A, A) + 2 * prodNums(A, B) + prodNums(B, B);
}
