export interface User {
  username: string;
}

export enum Action {
  SIGNIN = 'auth/SIGNIN',
  SIGNIN_SUCCESS = 'auth/SIGNIN_SUCCESS',
  SIGNIN_FAILURE = 'auth/SIGNIN_FAILURE',
}

export interface SigninRequestAction {
  type: Action.SIGNIN;
}
export interface SigninSuccessAction {
  type: Action.SIGNIN_SUCCESS;
  payload: AuthState & User;
}
export interface SigninFailureAction {
  type: Action.SIGNIN_FAILURE;
  payload: AuthState;
}

export type AuthState = {
  authenticated: boolean;
};
export type AuthAction =
  | SigninRequestAction
  | SigninSuccessAction
  | SigninFailureAction;
