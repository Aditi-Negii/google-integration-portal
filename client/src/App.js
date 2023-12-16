import './App.css';
import { Route, Routes } from 'react-router-dom';
import Home from "./Pages/Home";
import Signin from "./Pages/Signin";

function App() {
  return (
    <div className="App">
      <Routes>
          <Route path='/' element={<Signin/>}/>
          <Route path='/home' element={<Home/>}/>
        </Routes>
    </div>
  );
}

export default App;



