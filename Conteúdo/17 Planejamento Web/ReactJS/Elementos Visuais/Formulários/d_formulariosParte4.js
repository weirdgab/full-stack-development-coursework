class Usuario extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			indexCarro: 'mobi',
			textoCarro: '',
			obs: '',
		};
	}

	handleCampo = (campo) => {
		if (campo.target.type === 'select-one') {
			this.setState({
				textoCarro: campo.nativeEvent.target[campo.nativeEvent.target.selectedIndex].text,
				indexCarro: campo.target.value,
			});
		} else {
			this.setState({ [campo.target.name]: campo.target.value });
		}
	};

	render() {
		return (
			<>
				<form>
					<h1>Formulário - Parte 4</h1>
					<label>
						Escolha um carro:
						<select
							value={this.state.indexCarro}
							name="indexCarro"
							onChange={this.handleCampo}
						>
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
					<p>Carro Escolhido: {this.state.textoCarro}</p>
					<p>ID Carro Escolhido: {this.state.indexCarro}</p>
					<p>Observações: {this.state.obs}</p>
				</div>
			</>
		);
	}
}

ReactDOM.render(<Usuario />, document.getElementById('root'));
