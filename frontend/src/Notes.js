import React, { Component } from 'react';
import axios from 'axios';
import cookie from 'react-cookies';
import NoteForm from './NoteForm';

// import { Route, Link } from 'react-router-dom';

class Notes extends Component {

  constructor(props) {
    super(props);
    this.state = {
      notes: []
    };
  };

  newNote = (newnote) => {
    this.setState(prevState => ({
      notes: [...prevState.notes, newnote]
    }))
  }

  componentDidMount() {
    var theme_id = this.props.match.params.theme_id
    axios.get(`http://localhost:8000/api/theme/`+ theme_id + '/notes/', {
        headers: { Authorization: "Token " + cookie.load("token") }
    }).then(response => {
        this.setState({notes: response.data});
      })
  };

  render() {
    return (
      <div>
        <NoteForm newNote={this.newNote} theme_id={this.props.match.params.theme_id}/>
        <ul className='list-group'>
          {this.state.notes.map((note) =>
            <li className="list-group-item" key={note.index}>
              <h4 className="subtheme">{note.subtheme}</h4>
              <p className="textnote">{note.text}</p>
              <p className='footnote'>{note.footnote}</p>
            </li>
          )}
        </ul>
      </div>
    );
  }
}

export default Notes;
