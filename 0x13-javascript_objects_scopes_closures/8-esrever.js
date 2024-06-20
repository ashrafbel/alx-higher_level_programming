#!/usr/bin/node

exports.esrever = function (list) {
  const Rv = [];
  for (let a = list.length - 1; a >= 0; a--) {
    Rv.push(list[a]);
  }
  return Rv;
};
