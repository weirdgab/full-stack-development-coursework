import { useState } from 'react';
import { useDispatch } from 'react-redux';
import { changeUser } from '../redux/userSlice';

function Login() {
  const [nome, setNome] = useState('');
  const dispatch = useDispatch();

  return (
    <div>
      <input
        type="text"
        placeholder="Digite seu nome"
        value={nome}
        onChange={(e) => setNome(e.target.value)}
      />
      <button onClick={() => dispatch(changeUser(nome))}>Login</button>
    </div>
  );
}

export default Login;