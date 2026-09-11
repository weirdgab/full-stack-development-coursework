class Header extends React.Component {
	render() {
		return (
			<header className="cabecalho">
				<h1 className="boasVindas">Bem vindo {this.props.name}!</h1>
				<h2 className="titulo">Manipulando Componentes</h2>
			</header>
		);
	}
}

function Navegacao() {
	return <div className="navegacao">Barra de Navegação</div>;
}

function Principal() {
	return <div className="principal">Coluna Principal</div>;
}

function Rodape() {
	return (
		<footer className="rodape">
			<p>Rodapé</p>
		</footer>
	);
}

// Chamando um componente dentro de outro
// function ComposicaoComponentes() {
//	  return <Principal />;
// }

// Com mais de um componente é preciso encapsulá-los com a seguinte sintaxe:
// return (
//     <tag DOM>
//         <Componente_Classe_1 param1=´valor´ param2=´valor´ .../>
//     </tag DOM>
// );

function Topo(props) {
	return (
		<div className="topo">
			<Header name={props.name} />
			<Navegacao />
		</div>
	);
}

function App(props) {
	return (
		<div className="app">
			<Topo name={props.name} />
			<Principal />
			<Rodape />
		</div>
	);
}

ReactDOM.render(<App name="Marcelo" />, document.getElementById('root'));

// Adicionando fragmentos
// <React.Fragment>
//  	<Componente_A />
//  	<Componente_B />
//  	<Componente_C />
//  	<Componente_D />
// </React.Fragment>;

// Sintaxe simplificada
// <>
//      <Componente_A />
//      <Componente_B />
//      <Componente_C />
//      <Componente_D />
// </>
