import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {

  state = {
    image: null
  };

  handleImageChange = (e) => {
    this.setState({
      image: e.target.files[0]
    })
  };

  handleSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
    let form_data = new FormData();
    form_data.append('image', this.state.image, this.state.image.name);
    let url = 'http://localhost:5000/api/posts';
    const Upload = async() => {
      await axios
        .post(url, form_data)
        .then(res => console.log("res.data"))
        .catch(err => console.log(err))}
    Upload();
  };

  handleResult = (e) => {
    e.preventDefault();
    const Result = async() => {
      await axios
        .get('http://localhost:5000/api/results')
        .then(res => console.log(res.data))
        .catch(err => console.log(err))}
    Result()
  }  

  render() {
    return (
      <div className="App">
        <form onSubmit={this.handleSubmit}>
          <p>
            <input type="file"
                   id="image"
                   accept="image/png, image/jpeg"  onChange={this.handleImageChange} required/>
          </p>
          <input type="submit"/>
        </form>
        <button onClick={this.handleResult}>
          Say Hello
        </button>
      </div>
    );
  }
}

export default App;