class Usuario extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			nome: 'Antônio',
			sobrenome: 'Albuquerque',
			idade: 12,
			nacionalidade: 'Brasil',
		};
	}

	mudarUsuario() {
		this.setState({
			nome: this.props.usuario.name,
			idade: this.props.usuario.age,
		});
	}

	somarIdade() {
		this.setState({
			idade: this.state.idade + this.props.valor,
		});
	}

	render() {
		return (
			<>
				<h1>
					Nome Completo: {this.state.nome} {this.state.sobrenome}
				</h1>
				<h2>Idade: {this.state.idade}</h2>
				<h3>Nacionalidade: {this.state.nacionalidade}</h3>
				<button onClick={() => this.mudarUsuario()}>Mudar</button>
				<button onClick={() => this.somarIdade()}>Incrementar Idade</button>
			</>
		);
	}
}

const novoUsuario = { name: 'Juliana', age: 25 };

ReactDOM.render(<Usuario valor={1} usuario={novoUsuario} />, document.getElementById('root'));
