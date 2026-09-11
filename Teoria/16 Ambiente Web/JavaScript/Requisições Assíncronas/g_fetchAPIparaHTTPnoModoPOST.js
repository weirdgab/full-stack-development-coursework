async function postName() {
	const object = {
		name: 'James Gordon',
	};
	const response = await fetch('/api/names', {
		method: 'POST',
		body: JSON.stringify(object),
		headers: { 'Content-Type': 'application/json' },
	});
	const responseText = await response.text();
	console.log(responseText); //'OK'
}
postName();
