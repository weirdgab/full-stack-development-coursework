import React, { useState } from 'react';

import UsandoHookUseState from './Hooks/a_HookUseState';
import Incrementar from './Hooks/b_IncrementandoVariavel';
import UsandoHookUseEffect from './Hooks/d_HookUseEffect';

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
