#!/usr/bin/node
const square = require('./5-square');
module.exports = class Square extends square {
  charPrint (c) {
    const line = new Array(Number(this.width)).fill((c || 'X'));
    for (let i = 0; i < this.height; i++) {
      console.log(line.join(''));
    }
  }
};
