import * as React from 'react';
import type { AuthState, AuthAction } from './types';
import { Action } from './types';

const initialState: AuthState = {
  authenticated: false,
};

const reducer: React.Reducer<AuthState, AuthAction> = (state, action) => {
  switch (action.type) {
    case Action.SIGNIN:
      return {
        ...state,
      };
    case Action.SIGNIN_SUCCESS:
      return {
        ...state,
        authenticated: action.payload.authenticated,
      };
    case Action.SIGNIN_FAILURE:
      return {
        ...state,
        authenticated: action.payload.authenticated,
      };
    default:
      throw new Error('AuthAction');
  }
};

const useAuthReducer = (): [AuthState, React.Dispatch<AuthAction>] =>
  React.useReducer(reducer, initialState);

export default useAuthReducer;
