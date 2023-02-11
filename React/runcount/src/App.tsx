import React, { useState } from 'react';
import './App.css';
import SaveList from './components/SaveList';
import { Run } from "./models/Run";

const App: React.FC = () => {
  const [count, setCount] = useState(0);

  // Holds all the runs for App
  const [runs, setRuns] = useState<Run[]>([]);

  // Add run to list hook, using 'handle' naming convention
  const handleAdd = (e: React.FormEvent): void => {
    e.preventDefault();
    setRuns([
      ...runs,
      {
        id: 1,
        name: "Test Run",
        distance: 1,
      }
    ]);
    console.log(runs);
  }

  return (
    <div className="App">
      <h1>Welcome to Run Count!</h1>

      {/* <Run count={count}/> */}
      <SaveList 
        name={""}
        distance={0}
        handleAdd={handleAdd}
        />

      <hr></hr>

      {runs.map((run) => (
        <li>{run.name}</li>
      ))}
    </div>
  );
}

export default App;
