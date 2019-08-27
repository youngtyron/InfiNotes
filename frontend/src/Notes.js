import React, { Component } from 'react';
import axios from 'axios';
import { Route, Link } from 'react-router-dom';


class Notes extends Component {

  constructor(props) {
    super(props);
    this.state = {
      notes: []
    };
  };


  componentDidMount() {
    var theme_id = this.props.match.params.theme_id
    axios.get(`http://localhost:8000/api/notes/`+ theme_id)
      .then(response => {
        this.setState({notes: response.data});
      })
  };

  render() {
    return (
      <div>
        <ul className='list-group'>
          {this.state.notes.map((note) =>
            <li className="list-group-item" key={note.index}>
              <h4>{note.subtheme}</h4>
              <p>{note.text}</p>
              <p style={{fonеStyle: "oblique"}}>{note.footnote}</p>
            </li>
          )}
        </ul>
      </div>
    );
  }
}

export default Notes;
