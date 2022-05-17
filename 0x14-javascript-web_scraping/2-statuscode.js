#!/usr/bin/node

var axios = require('axios');
var req = axios({
    method: 'GET',
    url: process.argv[2],
});

req.catch((error) => {
    if (error.response) {
      console.log("code: "+error.response);
      process.exit();
    }
});

req.then(res => {
  if(res)
  {
    console.log("code: "+res.status);
    process.exit()
  }
});
