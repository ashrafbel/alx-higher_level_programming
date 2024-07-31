#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  const movi = JSON.parse(body);
  const chars = movi.characters;

  chars.forEach(characterUrl => {
    request(characterUrl, function (err, response, body) {
      if (err) {
        console.error(err);
        return;
      }
      const charJson = JSON.parse(body);
      console.log(charJson.name);
    });
  });
});
