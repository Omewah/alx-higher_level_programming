#!/usr/bin/node
// a class Rectangle that defines a rectangle

module.exports = class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && typeof h === 'number' && w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let b = 0;

      for (; b < this.width; b++) {
        process.stdout.write('X');
      }

      if (b === this.width) {
        console.log('');
      }
    }
  }
};
