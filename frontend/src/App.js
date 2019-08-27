import React from 'react';
import './App.css';
import './InfiNotes.scss';

import { BrowserRouter, Route, Link } from 'react-router-dom';
import Themes from './Themes';
import Auth from './Auth';
import Notes from './Notes';

function App() {
  return (
    <div className="App">
      <div className="container">
        <BrowserRouter>
          <header>
            <Link to="/themes">Themes</Link>
            <Link to="/login">Login</Link>
          </header>
          <div className="row">
            <Route path="/themes" exact component={Themes}/>
            <Route path="/login" exact component={Auth}/>
            <Route path="/notes/:theme_id" exact render={
              (props) => <Notes {...props}/>
            }/>
          </div>
        </BrowserRouter>
      </div>
    </div>
  );
}

export default App;
