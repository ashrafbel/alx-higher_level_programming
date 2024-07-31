#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

request(apiUrl, function (err, response, body) {
  if (err) {
    console.log(err);
    return;
  }

  const d = JSON.parse(body);
  let ctMouvie = 0;

  d.results.forEach(movie => {
    movie.characters.forEach(character => {
      if (character.includes(characterId)) {
        ctMouvie++;
      }
    });
  });

  console.log(ctMouvie);
});
