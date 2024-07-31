#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const fl_path = process.argv[3];

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  fs.writeFile(fl_path, body, 'utf-8', function (err) {
    if (err) {
      console.error(err);
    }
  });
});
