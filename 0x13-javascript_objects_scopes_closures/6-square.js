#!/usr/bin/node
const square1 = require('./5-square');
module.exports = class Square extends square1 {
  charPrint (c) {
    const line = new Array(Number(this.width)).fill((c || 'X'));
    for (let i = 0; i < this.height; i++) {
      console.log(line.join(''));
    }
  }
};
