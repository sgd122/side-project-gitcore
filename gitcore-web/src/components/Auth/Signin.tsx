import * as React from 'react';
import { useAuth, signin } from 'context/Auth';

interface InputState {
  username: string;
  password: string;
}

const initialState: InputState = {
  username: '',
  password: '',
};

const Signin: React.FC = () => {
  const [inputs, setInputs] = React.useState<InputState>(initialState);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setInputs({
      ...inputs,
      [name]: value,
    });
  };

  const { state, dispatch } = useAuth();

  return (
    <div>
      <input type="text" name="username" onChange={handleInputChange} />
      <input type="password" name="password" onChange={handleInputChange} />
      <button
        type="button"
        onClick={() => dispatch(signin(inputs.username, inputs.password))}
      >
        Signin
      </button>
      <span>{state.authenticated ? 'true' : 'false'}</span>
    </div>
  );
};

export default Signin;
