import React from 'react';
import './App.css';
import './InfiNotes.scss';
import cookie from 'react-cookies'
import { Component } from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';
import Themes from './Themes';
import Login from './Login';
import Logout from './Logout';
import Notes from './Notes';


class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      isLoggedIn: false
    };
  };

  componentDidMount(){
    if (cookie.load('token')){
      this.setState({isLoggedIn: true})
    }
  }

  updateLogged = (value) => {
    this.setState({ isLoggedIn: value })
  }

  render() {
    return (
      <div className="App">
        <div className="container">
          <BrowserRouter>
            <header>
              <Link to="/themes">Themes</Link>
              {this.state.isLoggedIn ? (
                <Logout updateLogged={this.updateLogged}/>
              ) : (
                <Link to="/login">Login</Link>
              )}
            </header>
            <div className="row">
              <Route path="/themes" exact component={Themes}/>
              {!this.state.isLoggedIn &&
                <Route path="/login" exact
                  render={(props) => <Login {...props} updateLogged={this.updateLogged} />
                }/>
              }
              <Route path="/notes/:theme_id" exact render={
                (props) => <Notes {...props}/>
              }/>
            </div>
          </BrowserRouter>
        </div>
      </div>
    );
  }
}

export default App;
