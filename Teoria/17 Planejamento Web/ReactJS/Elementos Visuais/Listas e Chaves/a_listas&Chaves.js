// Exemplo 1
function GerarElementos() {
	const carros = ['Strada', 'HB20', 'Mobi', 'Onix'];
	const listaCarros = carros.map((carro) => <li>{carro}</li>);

	return <ul>{listaCarros}</ul>;
}

ReactDOM.render(<GerarElementos />, document.getElementById('root'));
