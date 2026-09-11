class Usuario extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			carro: 'mobi',
			obs: '',
		};
	}

	handleCampo = (campo) => {
		this.setState({ [campo.target.name]: campo.target.value });
	};

	render() {
		return (
			<>
				<form>
					<h1>Formulário - Parte 3</h1>
					<label>
						Escolha um carro:
						<select value={this.state.carro} name="carro" onChange={this.handleCampo}>
							<option value="strata">Fiat Strada</option>
							<option value="hb20">Hyundai HB20</option>
							<option value="mobi">Fiat Mobi</option>
							<option value="onix">Chevrolet Onix</option>
						</select>
						<p>
							<textarea
								type="text"
								name="obs"
								onChange={this.handleCampo}
								placeholder="Deixe aqui uma observação"
							/>
						</p>
					</label>
				</form>
				<div>
					<p>Carro Escolhido: {this.state.carro}</p>
					<p>Observações: {this.state.obs}</p>
				</div>
			</>
		);
	}
}

ReactDOM.render(<Usuario />, document.getElementById('root'));
