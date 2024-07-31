#!/usr/bin/node

const request = require('request');
const u = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(u, function (err, resp, body) {
  data = JSON.parse(body);
  console.log(data.title);
});
