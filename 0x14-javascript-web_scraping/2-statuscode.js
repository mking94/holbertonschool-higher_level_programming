#!/usr/bin/node

const axios = require('axios');
const req = axios({
  method: 'GET',
  url: process.argv[2]
});
let check = 0;
req.catch((error) => {
  if (error.response) {
    console.log('code: ' + error.response);
    check = 1;
  }
});

req.then(res => {
  if (res && check === 0) {
    console.log('code: ' + res.status);
  }
});
