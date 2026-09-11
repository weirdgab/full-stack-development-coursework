// Definição de Classes:
class Pessoa {
	constructor(nome, idade) {
		this.nome = nome;
		this.idade = idade;
	}
	exibir = () => alert(`${this.nome} :: ${this.idade}`);
} // Sintaxe nova

function Pessa(nome, idade) {
	this.nome = nome;
	this.idade = idade;
	this.exibir = () => alert(`${this.nome} :: ${this.idade}`);
} // Sintaxe antiga

// Definição de objetos em JSON
const p = {
	nome: 'Ana',
	idade: 25,
	exibir() {
		alert(`${this.nome} :: ${this.idade}`);
	},
};
