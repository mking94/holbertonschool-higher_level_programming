#!/usr/bin/node
var filepath = process.argv[2];
var content = process.argv[3];
var fs = require('fs');
fs.writeFile(filepath , content, err => {
  if (err) {
    console.error(err);
  }
});
