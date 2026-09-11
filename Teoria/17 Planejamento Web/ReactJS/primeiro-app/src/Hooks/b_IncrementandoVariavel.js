import React, { useState } from 'react';

function Incrementar() {
	const [valor, setValor] = useState(0);

	function incrementarVariavel() {
		setValor(valor + 1);
	}

	const incrementa = () => {
		setValor(valor + 1);
	};

	return (
		<>
			<h1>Valor da Variável: {valor}</h1>
			<button onClick={incrementarVariavel}>Incrementar</button>
			<button onClick={incrementa}>Incrementar</button>
			<button onClick={() => setValor(valor + 1)}>Incrementar</button>
		</>
	);
}

export default Incrementar;
