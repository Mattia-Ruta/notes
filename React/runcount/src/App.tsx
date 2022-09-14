import React, { useState } from 'react';
import logo from './logo.svg';
import Run from "./components/Run";
import './App.css';
import SaveList from './components/Form';

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="App">
      <h1>Welcome to Run Count!</h1>

      <p>Current count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Add 1</button>

      <Run count={count}/>
      <SaveList />

    </div>
  );
}

export default App;
