#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    const line = new Array(Number(this.width)).fill('X');
    for (let i = 0; i < this.height; i++) {
      console.log(line.join(''));
    }
  }

  rotate () {
    this.width = Number(this.width) + Number(this.height);
    this.height = this.width - this.height;
    this.width = this.width - this.height;
  }

  double () {
    this.width = this.width * 2;
    this.height *= 2;
  }
};
