import React, { useState } from 'react';

function UsandoHookUseState() {
	const [nome, setNome] = useState('Jozie1');
	const [idade, setIdade] = useState(40);
	const [ligado, setLigado] = useState(true);
	const [todos, setTodos] = useState([{ nome: 'Joziel', idade: 40 }, { altura: 1.84 }]);

	return (
		<>
			<h1>
				Olá {nome}, sua idade é {idade} anos! {ligado ? 'Ligado' : 'Desligado'}
			</h1>
			<h1>Olá {todos[1].altura}</h1>
		</>
	);
}

export default UsandoHookUseState;
