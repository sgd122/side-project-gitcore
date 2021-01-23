import * as React from 'react';
import Signin from 'components/Auth';
import { useTheme, useChangeTheme } from 'context/Theme';

const App: React.FC = () => {
  const theme = useTheme();
  const changeTheme = useChangeTheme();

  const handlechangeTheme = () => {
    changeTheme(theme.colorScheme === 'light' ? 'dark' : 'light');
  };

  return (
    <div
      className="App"
      style={{
        padding: '1rem',
        backgroundColor: theme.palette.background,
        color: theme.palette.text,
      }}
    >
      <h1 style={{ color: theme.palette.primary }}>Hello, world!</h1>
      <h2 style={{ color: theme.palette.secondary }}>React TypeScript</h2>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
        veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
        commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
        velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
        occaecat cupidatat non proident, sunt in culpa qui officia deserunt
        mollit anim id est laborum.
      </p>
      <button type="button" onClick={handlechangeTheme}>
        Toggle Theme
      </button>
      <Signin />
    </div>
  );
};

export default App;
