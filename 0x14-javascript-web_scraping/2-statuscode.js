#!/usr/bin/node

const rt = require('request');
const u = process.argv[2];

rt(u, function (e, response, body) {
  if (e) {
    console.log(e);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
