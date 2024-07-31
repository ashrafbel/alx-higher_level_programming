#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (err, response, body) {
  if (err) {
    console.error(err);
    return;
  }
  const tasks = JSON.parse(body);
  const takscomplete = {};

  tasks.forEach(task => {
    if (task.completed) {
      if (!takscomplete[task.userId]) {
        takscomplete[task.userId] = 0;
      }
      takscomplete[task.userId]++;
    }
  });

  console.log(takscomplete);
});
