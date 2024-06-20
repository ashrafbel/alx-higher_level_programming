#!/usr/bin/node
const D = require('./100-data.js');
const L = D.list;
console.log(L);

const M = L.map((x, y) => x * y);
console.log(M);
