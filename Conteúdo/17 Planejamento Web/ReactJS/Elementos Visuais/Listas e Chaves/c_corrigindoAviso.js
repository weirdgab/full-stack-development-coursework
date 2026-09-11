function GerarElementos(props) {
	const elementos = props.arrayElementos;
	const listaElementos = elementos.map((e) => <li key={e.toString()}>{e}</li>);

	return <ul>{listaElementos}</ul>;
}

const minhaLista = ['Strada', 'HB20', 'Mobi', 'Onix'];

ReactDOM.render(<GerarElementos arrayElementos={minhaLista} />, document.getElementById('root'));
