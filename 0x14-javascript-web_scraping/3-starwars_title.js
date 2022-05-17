#!/usr/bin/node

const axios = require('axios');
axios({
  method: 'GET',
  url: 'https://swapi-api.hbtn.io/api/films/' + process.argv[2]
}).then(res => {
  if (res) {
    console.log(res.data.title);
  }
});
