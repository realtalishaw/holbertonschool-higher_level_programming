#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const j = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      i++;
    }
  }
  return j;
};
