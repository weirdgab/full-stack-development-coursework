// Sem JSX
class BoasVindasSemJSX extends React.Component {
	render() {
		return React.createElement('div', null, 'Olá, ', this.props.nome, '!');
	}
}

// Com JSX
class BoasVindasComJSX extends React.Component {
	render() {
		return <div>Olá, {this.props.nome}!</div>;
	}
}

ReactDOM.render(<BoasVindasComJSX nome="Alberto" />, document.getElementById('root'));
