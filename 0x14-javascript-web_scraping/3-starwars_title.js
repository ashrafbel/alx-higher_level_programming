#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request({ url: url, method: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const d = JSON.parse(body);
    console.log(d.title);
  }
});

