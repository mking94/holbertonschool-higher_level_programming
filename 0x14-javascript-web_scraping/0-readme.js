#!/usr/bin/node
const filePath = process.argv[2];
const fs = require('fs');
fs.readFile(filePath, { encoding: 'utf-8' }, function (err, data) {
  if (!err) {
    console.log(data);
  } else {
    console.log(err);
  }
});
