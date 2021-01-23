import * as React from 'react';
import type { ThemeState, ThemeAction } from './types';
import { Action } from './types';

const initialState: ThemeState = {
  scheme: 'light',
};

const reducer: React.Reducer<ThemeState, ThemeAction> = (state, action) => {
  switch (action.type) {
    case Action.CHANGE_THEME:
      return {
        ...state,
        scheme: action.payload.scheme,
      };
    default:
      throw new Error('ThemeAction');
  }
};

const useThemeReducer = (): [ThemeState, React.Dispatch<ThemeAction>] =>
  React.useReducer(reducer, initialState);

export default useThemeReducer;
