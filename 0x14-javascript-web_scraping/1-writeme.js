#!/usr/bin/node
const filepath = process.argv[2];
const content = process.argv[3];
const fs = require('fs');
fs.writeFile(filepath, content, err => {
  if (err) {
    console.error(err);
  }
});
