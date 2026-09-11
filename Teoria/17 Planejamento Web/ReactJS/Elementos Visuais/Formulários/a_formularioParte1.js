class Usuario extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			nome: '',
			idade: null,
		};
	}

	funcaoNome = (campoNome) => {
		this.setState({ nome: campoNome.target.value });
	};

	funcaoIdade = (campoIdade) => {
		this.setState({ idade: campoIdade.target.value });
	};

	render() {
		return (
			<>
				<form>
					<h1>Formulário - Parte 1</h1>
					<input type="text" placeholder="Nome" onChange={this.funcaoNome} />
					<label>
						<input type="number" onChange={this.funcaoIdade} />
					</label>
				</form>
				<div>
					<p>Nome: {this.state.nome}</p>
					<p>Idade:{this.state.idade}</p>
				</div>
			</>
		);
	}
}

ReactDOM.render(<Usuario />, document.getElementById('root'));
