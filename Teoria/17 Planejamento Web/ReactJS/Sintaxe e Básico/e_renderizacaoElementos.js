function tick() {
	const element = (
		<div>
			<h1>Olá, Mundo!</h1>
			<h2>Agora são {new Date().toLocaleDateString()}.</h2>
		</div>
	);

	ReactDOM.render(element, document.getElementById('root'));
}

setInterval(tick, 1000);
