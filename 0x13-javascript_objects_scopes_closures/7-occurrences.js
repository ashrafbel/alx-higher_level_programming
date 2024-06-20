#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let C = 0;
  for (const a = 0; a < list.length; a++) {
    if (list[a] === searchElement) {
      C++;
    }
  }
  return C;
};
