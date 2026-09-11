class Contador extends React.Component {
	constructor(props) {
		super(props);
		this.state = { numero: 0 };
	}

	incrementar() {
		this.setState({ numero: this.state.numero + 1 });
	}

	render() {
		return (
			<>
				<h2>O valor do número é {this.state.numero}</h2>
				<button onClick={() => this.incrementar()}>Incrementar</button>
			</>
		);
	}
}

ReactDOM.render(<Contador />, document.getElementById('root'));

// PROBLEMA: Usar intuitivamente o código abaixo para atualizar um estado
// this.state.numero = this.state.numero + 1;

// MOTIVO: o componente não será renderizado novamente

// SOLUÇÃO: usar sempre o setState para atualizar o valor.

// PROBLEMA: usar o código abaixo para sincronizar os estados:
// this.setState({ numero: this.state.numero + this.props.outroValor });
// MOTIVO: o React pode agrupar várias chamadas setStates em uma única atualização na aplicação.

// SOLUÇÃO 1: reescrever o parâmetro como uma função que terá como primeiro parâmetro o estado anterior
// e como segundo as propriedades:
// this.setState(function (state, props) {
//     return {
//         numero. state.numero + props.outroValor
//     };
// });

// SOLUÇÃO 2: fazer isso com uma notação com arrow functions:
// this.setState((state, props) => ({
// 	  numero: state.numero + state.outroValor
// }));
