#!/usr/bin/node

const rt = require('request');
const u = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

rt(u, function (err, resp, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
