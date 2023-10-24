#!/usr/bin/node

const request = require('request');
const fcont = require('fcont');

request(process.argv[2], function (_err, _res, body) {
  fcont.writeFile(process.argv[3], body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
