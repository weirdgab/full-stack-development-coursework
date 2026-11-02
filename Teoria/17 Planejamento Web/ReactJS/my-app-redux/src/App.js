import Login from './components/Login';
import Logout from './components/Logout';
import User from './components/User';

function App() {
  return (
    <div>
      <h1>Redux: login e logout</h1>
      <User />
      <Login />
      <Logout />
    </div>
  );
}

export default App;