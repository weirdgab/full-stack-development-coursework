// JavaScript Procedural
const meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril'];
let copiaMeses = [];
for (let i = 0; i < meses.length; i++) {
	copiaMeses[i] = 'Mês de ' + meses[i];
}

// Formato Declarativo
const meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril'];
let copiaMeses = meses.map((mes) => 'Mês de ' + mes);
