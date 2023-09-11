#!/usr/bin/node
// a script that computes and prints a factorial
// The first argument is integer (argument can be cast as integer) used for computing the factorial
// Factorial of NaN is 1

function factorial (a) {
  return a === 0 || isNaN(a) ? 1 : a * factorial(a - 1);
}

console.log(factorial(Number(process.argv[2])));
