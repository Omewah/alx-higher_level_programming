#!/usr/bin/node
// a script that prints a square
// The first argument is the size of the square
// If the first argument can’t be converted to an integer, print “Missing size”

const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let a = 0; a < size; a++) {
    let row = '';
    for (let b = 0; b < size; b++) row += 'X';
    console.log(row);
  }
}
