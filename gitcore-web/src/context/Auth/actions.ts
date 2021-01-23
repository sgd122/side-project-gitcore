import type {
  AuthAction,
  SigninRequestAction,
  SigninFailureAction,
  SigninSuccessAction,
} from './types';
import { Action } from './types';

const signinRequest = (): SigninRequestAction => {
  return {
    type: Action.SIGNIN,
  };
};

const signinSuccess = (username: string): SigninSuccessAction => {
  return {
    type: Action.SIGNIN_SUCCESS,
    payload: {
      authenticated: true,
      username,
    },
  };
};

const signinFailure = (): SigninFailureAction => {
  return {
    type: Action.SIGNIN_FAILURE,
    payload: {
      authenticated: false,
    },
  };
};

// eslint-disable-next-line import/prefer-default-export
export const signin = (username: string, password: string): AuthAction => {
  signinRequest();

  // STUB
  return username === password ? signinSuccess(username) : signinFailure();
};
