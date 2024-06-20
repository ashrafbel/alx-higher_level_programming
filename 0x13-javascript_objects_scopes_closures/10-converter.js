#!/usr/bin/node

exports.converter = function (base) {
  return function (N) {
    return N.toString(base);
  }
}
