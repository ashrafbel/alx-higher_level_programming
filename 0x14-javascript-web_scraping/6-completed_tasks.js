#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  const taskat = JSON.parse(body);
  const comleteTask = {};

  taskat.forEach(task => {
    if (taskat.completed) {
      if (!comleteTask[taskat.userId]) {
        comleteTask[taskat.userId] = 0;
      }
      comleteTask[taskat.userId]++;
    }
  });

  console.log(comleteTask);
});
