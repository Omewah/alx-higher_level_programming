#!/usr/bin/node
// a script that prints My number: <first argument converted in integer>

const myNum = Math.floor(Number(process.argv[2]));
console.log(isNaN(myNum) ? 'Not a number' : `My number: ${myNum}`);
