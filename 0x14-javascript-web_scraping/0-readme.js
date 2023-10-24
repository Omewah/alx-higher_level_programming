#!/usr/bin/node

const fcont = require('fcont');

fcont.readFile(process.argv[2], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
