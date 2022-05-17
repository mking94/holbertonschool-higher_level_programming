#!/usr/bin/node

var axios = require('axios');
var req = axios({
    method: 'GET',
    url: process.argv[2],
});

req.then(res => {
  if(res)
  {
    console.log(res.data.title);
  }
});
