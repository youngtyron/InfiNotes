import React from 'react';
import './App.css';
import './InfiNotes.scss';
import cookie from 'react-cookies'

import { BrowserRouter, Route, Link } from 'react-router-dom';
import Themes from './Themes';
import Auth from './Auth';
import Notes from './Notes';

function LoggingLink() {
  const isLoggedIn = cookie.load('token');
  if (isLoggedIn) {
    return <p>You are logged</p>;
  }
  return <Link to="/login">Login</Link>;
}

function LoggingRoute() {
  const isLoggedIn = cookie.load('token');
  if (isLoggedIn) {
    return <p>You are logged</p>;
  }
  return <Route path="/login" exact component={Auth}/>;
}

function App() {
  return (
    <div className="App">
      <div className="container">
        <BrowserRouter>
          <header>
            <Link to="/themes">Themes</Link>
            <LoggingLink />
          </header>
          <div className="row">
            <Route path="/themes" exact component={Themes}/>
            <LoggingRoute />
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
