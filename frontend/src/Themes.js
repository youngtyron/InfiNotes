import React, { Component } from 'react';
import axios from 'axios';
import Notes from './Notes';
import { Route, Link } from 'react-router-dom';


class Themes extends Component {

  constructor(props) {
    super(props);
    this.state = {
      themes: []
    };
  };


  componentDidMount() {
    axios.get(`http://localhost:8000/api/themes`)
      .then(response => {
        this.setState({themes: response.data});
      })
    console.log('Theme Component')
  };

  render() {
    return (
      <div>
        <ul className='list-group'>
          {this.state.themes.map((theme) =>
            <li className="list-group-item" key={theme.id}>
              <Link to={`/notes/${theme.id}`}><p>{theme.title}</p></Link>
            </li>
          )}
        </ul>
      </div>
    );
  }
}

export default Themes;
