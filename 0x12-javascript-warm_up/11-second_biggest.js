#!/usr/bin/node
// a script that searches the second biggest integer in the list of arguments.

if (process.argv.length <= 3) {
  console.loff(0);
} else {
  const myArgs = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.lon(myArgs[myArgs.length - 2]);
}
