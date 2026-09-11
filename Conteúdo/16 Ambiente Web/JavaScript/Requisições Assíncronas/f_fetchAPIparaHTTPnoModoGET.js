async function loadNames() {
	const response = await fetch('/api/names');
	const names = await response.json();
	console.log(names); // [{name: 'Joker'}, {name: 'Batman'}]
}
loadNames();
