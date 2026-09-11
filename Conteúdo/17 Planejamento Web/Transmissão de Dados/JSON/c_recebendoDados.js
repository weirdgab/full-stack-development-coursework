// Representa um texto JSON (que poderia ter sido recebido de uma requisição, por ex)
var textoJson =
	'{"agencia": "5678-9", "tipo": "física", "nome": "Maria José", "numero": "222.222-22"}';

// Converte o texto JSON em um objeto Javascript
var objetoJS = JSON.parse(textoJson);

// Exibe na tag html com id=resultado os dados da conta
document.getElementById('resultado').innerHTML =
	'Agência: ' + objetoJS.agencia + ' Tipo: ' + objetoJS.tipo + ' Nome: ' + objetoJS.numero;
