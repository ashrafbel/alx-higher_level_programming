#!/usr/bin/node


const fs = require('fs');

const fl_path = process.argv[2];
fs.readFile(fl_path, 'utf8', (e, d) => {
  if (e) {
    console.error(e);
    return;
  }
  console.log(d);
});

