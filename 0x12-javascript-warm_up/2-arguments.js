#!/usr/bin/node
// prints a message depending of the number of arguments passed

const counter = process.argv.length;
console.log(counter === 2? 'No argument' : counter === 3? 'Argument found' : 'Arguments found');
