#!/usr/bin/node

const request = require('request');
const urlFilms = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(urlFilms, function (err, response, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
