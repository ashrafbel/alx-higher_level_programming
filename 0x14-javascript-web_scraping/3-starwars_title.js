#!/usr/bin/node

const rt = require('request');
const urlFilms = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(urlFilms, function (err, resp, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
