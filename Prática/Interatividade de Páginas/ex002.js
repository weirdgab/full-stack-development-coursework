var a = 5;
var b = -1;

if (a > b && b > 0) {
	console.log(
		'A primeira variável é maior que a segunda e a segunda variável é um número positivo.',
	);
} else if (a > b && b <= 0) {
	console.log('A primeira variável é maior que a segunda e a segunda não é um número positivo.');
} else if (a < b || b > 0) {
	console.log(
		'A primeira variável é menor que a segunda ou a segunda variável é um número positivo.',
	);
}
