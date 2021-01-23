import * as React from 'react';
import type { ColorScheme, Theme, ThemeAction } from './types';
import { changeTheme } from './actions';
import useThemeReducer from './reducers';

export const ThemeContext = React.createContext<Theme | null>(null);
export const DispatchContext = React.createContext<React.Dispatch<ThemeAction>>(
  () => {
    throw new Error('ThemeProvider');
  }
);

interface Props {
  children: React.ReactNode;
}

export const ThemeProvider: React.FC<Props> = ({ children }: Props) => {
  const [themeOptions, dispatch] = useThemeReducer();

  React.useEffect(() => {
    if (typeof window !== 'undefined') {
      if (window.matchMedia('(prefers-color-scheme: dark)')) {
        dispatch(changeTheme('dark'));
      } else {
        dispatch(changeTheme('light'));
      }
    }
  }, [dispatch]);

  const { scheme } = themeOptions;

  const theme = React.useMemo(() => {
    const nextTheme: Theme = {
      colorScheme: scheme,
      palette: {
        primary: scheme === 'light' ? '#5f4b8b' : '#00abc0',
        secondary: scheme === 'light' ? '#939597' : '#f0eee9',
        background: scheme === 'light' ? '#fafafa' : '#212121',
        text: scheme === 'light' ? 'rgba(0, 0, 0, 0.87)' : '#fff',
      },
    };
    return nextTheme;
  }, [scheme]);

  return (
    <ThemeContext.Provider value={theme}>
      <DispatchContext.Provider value={dispatch}>
        {children}
      </DispatchContext.Provider>
    </ThemeContext.Provider>
  );
};

export const useTheme = (): Theme => {
  const theme = React.useContext(ThemeContext);
  if (!theme) throw new Error('ThemeProvider');
  return theme;
};

export const useChangeTheme = (): ((scheme: ColorScheme) => void) => {
  const dispatch = React.useContext(DispatchContext);
  return React.useCallback((scheme) => dispatch(changeTheme(scheme)), [
    dispatch,
  ]);
};
