import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {

  state = {
    emotiontext: "",
    checked: true,
    image: null,
    result: ""
  };

  handleCheckChange = (e) => {
    this.setState({
      checked: !this.state.checked
    })
  };

  handleImageChange = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };

  handleTextChange = (e) => {
    this.setState({
      emotiontext: e.target.value
    })
  }

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('image', this.state.image, this.state.image.name);
    form_data.append('will', this.state.checked);
    form_data.append('emotion', this.state.emotiontext);
    let url = 'http://localhost:5000/api/posts';
    const Upload = async() => {
      await axios
        .post(url, form_data, {
          headers: {
            'content-type': 'multipart/form-data'
          }
        })
        .then(res => console.log(res.data))
        .catch(err => console.log(err.data))}
    Upload();
  };

  handleResult = (e) => {
    e.preventDefault();
    let url = 'http://localhost:5000/api/results';
    const Result = async() => {
      await axios
        .get(url)
        .then(res => this.setState({result: res.data}))
        .catch(err => this.setState({result: "error"}))}
    Result();
  };

  play = (e) => {
    e.preventDefault();
    let audio = new Audio('http://localhost:5000/test.mp3');
    audio.play();
    audio = null;
  }

  render() {
    return (
      <div className="App">
        <form onSubmit={this.handleSubmit}>
          <p>
            <input type="file"
                   id="image"
                   accept="image/png, image/jpeg, image/tif, image/tiff, .tif"  onChange={this.handleImageChange} required/>
          </p>
          Please Describe your current situation
            <p>
              <textarea rows = "20" onChange={this.handleTextChange}></textarea>
            </p>
          <p>
            <input
              type="checkbox"
              checked={this.state.checked}
              onChange={this.handleCheckChange}/>
              I am willing to share my personal data.
          </p>
          <input type="submit"/>
        </form>
        <button onClick={this.handleResult}>
          Get the result
        </button>
        <p>{this.state.result}</p>
        <button onClick={this.play.bind(this)}>Play</button>
      </div>
    );
  }
}

export default App;