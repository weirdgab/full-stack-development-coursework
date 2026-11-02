import { useDispatch } from 'react-redux';
import { logout } from '../redux/userSlice';

function Logout() {
  const dispatch = useDispatch();

  return <button onClick={() => dispatch(logout())}>Logout</button>;
}

export default Logout;