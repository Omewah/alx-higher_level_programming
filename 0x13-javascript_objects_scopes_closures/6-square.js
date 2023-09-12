#!/usr/bin/node
// defines a square and inherits from Square of 5-square.js

const Squaremod = require('./4-rectangle');

module.exports = class Square extends Squaremod {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
