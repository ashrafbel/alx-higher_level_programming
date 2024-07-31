#!/usr/bin/node

const fs = require('fs');
const fl_path = process.argv[2];

fs.readFile(fl_path, 'utf8', function (e, d) {
  if (e) {
    console.log(e);
  } else {
    process.stdout.write(d);
  }
});
