// Evento em html
<button onclick="enviarForm()">Enviar formulário</button>;

// Mesmo evento em React
<button onClick={enviarForm}>Enviar formulário</button>;

// Evitando que uma nova página fosse aberta em html
<a href="#" onclick="console.log('Link clicado'); return false">
	Link
</a>;

// Agora em React
function LinkClick() {
	function handleClick() {
		console.log('Link clicado');
	}

	return (
		<a href="#" onClick={handleClick}>
			Link
		</a>
	);
}

// Adicionando o preventDefault() e uma ligação com o bind
function LinkClick() {
	function handleClick(e) {
		e.preventDefault();
		console.log('Link clicado');
	}

	return (
		<a href="#" onClick={handleClick.bind()}>
			Link
		</a>
	);
}

// Adicionando arrow functions
function LinkClick() {
	function handleClick() {
		console.log('Link clicado');
	}

	return (
		<a href="#" onClick={() => handleClick()}>
			Link
		</a>
	);
}

// Definindo as entradas necessárias por meio de arrow functions em caso de necessidade de parâmetros
function LinkClick() {
	function handleClick(param1, param2) {
		console.log('Link clicado ' + param1 + ' ' + param2);
	}

	const param2 = 'B';

	return (
		<a href="#" onClick={() => handleClick('A', param2)}>
			Link
		</a>
	);
}
