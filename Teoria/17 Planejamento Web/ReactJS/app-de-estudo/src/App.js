import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import UsandoHookUseState from './Exemplos/UsandoHookUseState';
import IncrementandoVariavel from './Exemplos/IncrementandoVariavel';
import UsandoHookUseEffect from './Exemplos/UsandoHookUseEffect';
import UsandoFetchAPI from './Exemplos/UsandoFetchAPI';
import UsandoAxios from './Exemplos/UsandoAxios';
import UsandojQuery from './Exemplos/UsandojQuery';

function App() {
  return (
    <>
      <header>
        <h1>EnsineMe React</h1>
        <nav>
          <Link to="/">Home</Link> |{' '}
          <Link to="/hookUseState">Página 1</Link> |{' '}
          <Link to="/increment">Página 2</Link> |{' '}
          <Link to="/hookUseEffect">Página 3</Link> |{' '}
          <Link to="/fetch">Página 4</Link> |{' '}
          <Link to="/axios">Página 5</Link> |{' '}
          <Link to="/jQuery">Página 6</Link>
        </nav>
      </header>
      <main className="conteúdo-principal">
        <Routes>
          <Route path="/" element={<h2>Escolha uma página no menu</h2>} />
          <Route path="/hookUseState" element={<UsandoHookUseState />} />
          <Route path="/increment" element={<IncrementandoVariavel />} />
          <Route path="/hookUseEffect" element={<UsandoHookUseEffect />} />
          <Route path="/fetch" element={<UsandoFetchAPI />} />
          <Route path="/axios" element={<UsandoAxios />} />
          <Route path="/jQuery" element={<UsandojQuery />} />
        </Routes>
      </main>
    </>
  );
}

export default App;