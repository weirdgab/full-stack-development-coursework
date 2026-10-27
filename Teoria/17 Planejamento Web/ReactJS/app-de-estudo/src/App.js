import React, { useState } from 'react';

import UsandoHookUseState from './Exemplos/UsandoHookUseState';
import Incrementar from './Exemplos/IncrementandoVariavel';
import UsandoHookUseEffect from './Exemplos/UsandoHookUseEffect';

function App() {
	const [visivel, setVisivel] = useState(true);

	setTimeout(() => {
		setVisivel(false);
	}, 5000);

	return (
		visivel && (
			<>
				<UsandoHookUseEffect />
				<Incrementar />
				<UsandoHookUseEffect />
			</>
		)
	);
}

export default App;
