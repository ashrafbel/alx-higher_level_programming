#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let Ct = 0;

  for (let a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      Ct++;
    }
  }
  return Ct;
};
