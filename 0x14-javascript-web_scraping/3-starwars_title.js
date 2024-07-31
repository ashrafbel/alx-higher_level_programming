#!/usr/bin/node

const request = require('request');
const u = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(u, function (e, resp, body) {
  d = JSON.parse(body);
  console.log(d.title);
});
