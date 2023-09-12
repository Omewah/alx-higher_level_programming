#!/usr/bin/node
// prints the number of arguments already printed and the new argument value

const list = require('./100-data');
const newList = list.map((value, index) => value * index);

console.log(list);
console.log(newList);
