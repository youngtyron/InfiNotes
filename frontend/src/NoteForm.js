import React, { Component } from 'react';
import axios from 'axios';
import cookie from 'react-cookies';


class NoteForm extends Component {

  constructor(props) {
    super(props);
    this.state = {
            subtheme: '',
            text: '',
            footnote: ''
          };

    this.handleChangeSubtheme = this.handleChangeSubtheme.bind(this);
    this.handleChangeText = this.handleChangeText.bind(this);
    this.handleChangeFootnote = this.handleChangeFootnote.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChangeSubtheme(event) {
    this.setState({subtheme: event.target.value});
  };
  handleChangeText(event) {
    this.setState({text: event.target.value});
  };
  handleChangeFootnote(event) {
    this.setState({footnote: event.target.value});
  };

  handleSubmit = (event) => {
    event.preventDefault();
    var theme_id = this.props.theme_id
    axios.post(`http://localhost:8000/api/theme/`+theme_id+'/create/', {
        subtheme: this.state.subtheme,
        text: this.state.text,
        footnote: this.state.footnote
      },
      {
        headers: { Authorization: "Token " + cookie.load("token") }
    }).then(response => {
        console.log(response)
        this.props.newNote(response.data)
        // this.setState({notes: response.data});
      })
  };

  render() {
    return (
      <div className="col">
          <form onSubmit={this.handleSubmit}>
            <div className="form-group">
              <label htmlFor="exampleInputSubtheme">Subtheme</label>
              <input type="text" value={this.state.subtheme} onChange={this.handleChangeSubtheme} className="form-control" id="exampleInputSubtheme" aria-describedby="subthemeHelp" placeholder="Enter subtheme"/>
            </div>
            <div className="form-group">
              <label htmlFor="exampleInputText">Text</label>
              <input type="text" value={this.state.text} onChange={this.handleChangeText} className="form-control" id="exampleInputText" aria-describedby="textHelp" placeholder="Enter text"/>
            </div>
            <div className="form-group">
              <label htmlFor="exampleInputFootnote">Footnote</label>
              <input type="text" value={this.state.footnote} onChange={this.handleChangeFootnote} className="form-control" id="exampleInputFootnote" aria-describedby="footnoteHelp" placeholder="Enter footnote"/>
            </div>
            <button type="submit" className="btn btn-primary">Submit</button>
          </form>
      </div>
    );
  }
}

export default NoteForm;
