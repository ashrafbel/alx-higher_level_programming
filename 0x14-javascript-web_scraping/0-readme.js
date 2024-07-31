#!/usr/bin/node

const fs = require('fs');

fl_path = process.argv[2]
fs.readFile(fl_path, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    process.stdout.write(data);
  }
});
