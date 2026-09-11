// Cria uma variável para receber o conteúdo armazenado com localStorage
var jsonText = localStorage.getItem('stringJSON');

// Converte em um objeto JavaScript
jsObj = JSON.parse(jsonText);

// Exibe o conteúdo do objeto JS com o alert
alert(
	'Agência: ' +
		jsObj.agencia +
		' Tipo: ' +
		jsObj.tipo +
		' Nome: ' +
		jsObj.nome +
		' Número: ' +
		jsObj.numero,
);
