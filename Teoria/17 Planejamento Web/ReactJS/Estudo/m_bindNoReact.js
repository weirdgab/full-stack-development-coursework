// Exemplo 1: javascript puro
function exibirContexto() {
	console.log(this);
}

let usuario = {
	nome: 'João',
	idade: 20,
	nacionalidade: 'Brasil',
};

exibirContexto();

let bindUsuario = exibirContexto.bind(usuario);
bindUsuario();

// Exemplo 2: React
class Usuario extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			nome: 'Daniel',
			idade: 12,
		};
		this.bindMudarUsuario = this.bindMudarUsuario.bind(this);
	}
	mudarUsuario() {
		this.setState({
			nome: this.props.usuario.name,
			idade: this.props.usuario.age,
		});
	}
	render() {
		return (
			<>
				<h1>Nome Completo: {this.state.nome}</h1>
				<h2>Idade: {this.state.nome}</h2>
				<button onClick={this.bindMudarUsuario}>Mudar</button>
			</>
		);
	}
}

const novoUsuario = {
	name: 'Juliana',
	age: 25,
};

ReactDOM.render(<Usuario usuario={novoUsuario} />, document.getElementById('root'));
