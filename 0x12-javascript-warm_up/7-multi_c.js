#!/usr/bin/node
// a script that prints x times “C is fun”

const x = Math.floor(Number(process.argv[2]));
if (isNaN(x)) {
    console.log('Missing number of occurences');
} else {
    for (let a = 0; a < x; a++) {
        console.log('C is fun');
    }
}
