#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (e, d) {
  if (e) {
    console.log(e);
  } else {
    process.stdout.write(d);
  }
});
