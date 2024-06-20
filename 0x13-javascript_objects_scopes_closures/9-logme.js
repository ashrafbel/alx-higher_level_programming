#!/usr/bin/node

let Ct = 0;
exports.logMe = function (item) { console.log(`${Ct++}: ${item}`); };
