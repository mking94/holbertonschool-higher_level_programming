#!/usr/bin/node

const axios = require('axios');
const req = axios({
  method: 'GET',
  url: process.argv[2]
}).then(res => {
  if (res) {
    console.log('code: ' + res.status);
  }
}).catch(error => {
  if (error.response) {
    console.log('code: ' + error.response.status);
  }
});
