class BemVindo extends React.Component {
	render() {
		return <h1>Olá, {this.props.name}</h1>;
	}
}

const element = <BemVindo name="Rodrigo" />;

ReactDOM.render(element, document.getElementById('root'));
