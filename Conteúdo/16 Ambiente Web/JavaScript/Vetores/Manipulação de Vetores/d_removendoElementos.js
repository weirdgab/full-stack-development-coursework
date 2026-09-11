//Remoção de elementos
delete alunos[0]; //Método delete
console.log(alunos); //Imprimirá 'Helena', 'João', 'Carlos', 'Jenifer'

alunos.pop(); //Método pop, remove sempre o último elemento
console.log(alunos); //Imprimirá 'Helena', 'João', 'Carlos'

alunos.shift(); //Método shift, remove sempre o primeiro elemento
console.log(alunos); //Imprimirá 'João', 'Carlos'

var primos = [2, 3, 5, 7, 11, 13, 17];
alert(primos.length); //Imprimirá 7
primos.length = 4;
console.log(primos.length); //Imprimirá 4
