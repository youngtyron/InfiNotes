import React, { Component } from 'react';
import axios from 'axios';
import cookie from 'react-cookies';

class Logout extends Component {
  constructor(props) {
    super(props);
    this.state = {
    };
  };

  logout = () => {
    axios.get(`http://localhost:8000/logout/`, {
        headers: { Authorization: "Token " + cookie.load("token") }
    })
      .then(response => {
        cookie.remove('token');
        this.props.updateLogged(false)
      })
  }

  render() {
    return (
      <div>
          <button onClick={this.logout} className="btn btn-success">Logout</button>
      </div>
    );
  }
}

export default Logout;
