// A funções anteriores são idênticas exceto pelo campo, então podemos nomear os elementos e, dentro
// do nosso estado, utilizá-los:
class Usuario extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			nome: '',
			idade: null,
		};
	}

	handleCampo = (campo) => {
		this.setState({ [campo.target.name]: campo.target.value });
	};

	render() {
		return (
			<>
				<form>
					<h1>Formulário - Parte 2</h1>
					<input type="text" placeholder="Nome" name="nome" onChange={this.handleCampo} />
					<label>
						<input type="number" name="idade" onChange={this.handleCampo} />
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
