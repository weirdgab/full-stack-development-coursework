import { useSelector } from 'react-redux';
import { selectUser } from '../redux/userSlice';

function User() {
  const user = useSelector(selectUser);

  if (!user.isLogged) {
    return <p>Nenhum usuário logado</p>;
  }

  return <p>Usuário logado: {user.name}</p>;
}

export default User;