const user = {
	firstName: 'Dev',
	lastName: 'ReactJS',
};

function formatName(user) {
	return user.firstName + ' ' + user.lastName;
}

function getGreeting(user) {
	if (user) {
		return (
			<h1>
				Olá, {formatName(user)}, <p>o valor de PI é {Math.PI}</p>
			</h1>
		);
	}
	return <h1>Olá, desconhecido, qual seu nome?</h1>;
}

ReactDOM.render(
	getGreeting({
		firstName: 'Desenvolvedor(a)',
		lastName: 'ReactJS',
	}),
	document.getElementById('root'),
);
