#!/usr/bin/node

exports.converter = function (base) {
  function v (N) {
    return N.toString(base);
  }
  return v;
};
