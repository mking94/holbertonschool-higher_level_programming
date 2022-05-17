#!/usr/bin/node
const axios = require('axios');
const fs = require('fs');
axios({
  method: 'GET',
  url: process.argv[2]
}).then(res => {
  if (res) {
    const content = res.data;
    fs.writeFile(process.argv[3], content, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
