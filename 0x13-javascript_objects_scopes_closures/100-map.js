#!/usr/bin/node
// prints the number of arguments already printed and the new argument value

const arr = require('./100-data').list;

console.log(arr);
console.log(arr.map((x, idx) => x * idx));
