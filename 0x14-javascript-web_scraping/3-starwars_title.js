#!/usr/bin/node
const request = require('request');
const u = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request({ url: u, methods: 'GET' }, function (e, response, body) {
  if (e) {
    console.log(e);
  } else {
    b = JSON.parse(body);
    console.log(b.title);
  }
});
