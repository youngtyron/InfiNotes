import React, { Component } from 'react';
import axios from 'axios';
import cookie from 'react-cookies'

class Auth extends Component {

  constructor(props) {
    super(props);
    this.state = {
              username: '',
              password: '',
            };

    this.handleChangeUsername = this.handleChangeUsername.bind(this);
    this.handleChangePassword = this.handleChangePassword.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }




  handleChangeUsername(event) {
    this.setState({username: event.target.value});
  };

  handleChangePassword(event) {
    this.setState({password: event.target.value});
  };

  handleSubmit(event) {
    event.preventDefault();
    axios.post(`http://localhost:8000/api-token-auth/`, {
        username: this.state.username,
        password: this.state.password
      })
     .then(response => {
       var token = response.data['token']
       cookie.save('token', token)
    });

  };

  componentDidMount() {

  }

  render() {
    return (
      <div className="col">
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <label htmlFor="exampleInputUsername">Username</label>
              <input type="text" value={this.state.username} onChange={this.handleChangeUsername} className="form-control" id="exampleInputUsername" aria-describedby="usernameHelp" placeholder="Enter username"/>
            </div>
            <div className="form-group">
              <label htmlFor="exampleInputPassword1">Password</label>
              <input type="password" value={this.state.password} onChange={this.handleChangePassword} className="form-control" id="exampleInputPassword1" placeholder="Password"/>
            </div>
            <div className="form-check">
              <input type="checkbox" className="form-check-input" id="exampleCheck1"/>
              <label className="form-check-label" htmlFor="exampleCheck1">Check me out</label>
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
          </form>
      </div>
    );
  }
}

export default Auth;
