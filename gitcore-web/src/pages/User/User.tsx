import * as React from 'react';
import useAxios from 'axios-hooks';

export interface DetailData {
  id: number;
  gendar: string;
  login_method: string;
  username: string;
}

interface Data {
  results: Array<DetailData>;
}

const User: React.FC = () => {
  const [{ data, loading, error }, refetch] = useAxios<Data>(
    'http://localhost:8000/users/'
  );

  const onClick = () => {
    return refetch();
  };

  return (
    <div>
      User Page
      <button onClick={() => onClick()}>새로고침</button>
      <hr />
      {loading && 'loading...'}
      {error && error.message}
      <hr />
      {data && JSON.stringify(data.results)}
    </div>
  );
};

export default User;
