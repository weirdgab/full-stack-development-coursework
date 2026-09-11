// Componentes funcionais
function BemVindoFuncional(props) {
	return <h1>Olá, {props.name}!</h1>;
}

// Componentes de classe
class BemVindoClasse extends React.Component {
	render() {
		return <h1>Olá, {this.props.name}</h1>;
	}
}

ReactDOM.render(<BemVindoFuncional name="Rodrigo" />, document.getElementById('root'));
