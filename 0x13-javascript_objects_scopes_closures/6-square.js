#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  charPrint (c) {
    const line = new Array(Number(this.width)).fill((c || 'X'));
    for (let i = 0; i < this.height; i++) {
      console.log(line.join(''));
    }
  }
};
