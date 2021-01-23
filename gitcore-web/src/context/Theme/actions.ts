import type { ColorScheme, ThemeChangeAction } from './types';
import { Action } from './types';

// eslint-disable-next-line import/prefer-default-export
export const changeTheme = (scheme: ColorScheme): ThemeChangeAction => ({
  type: Action.CHANGE_THEME,
  payload: {
    scheme,
  },
});
