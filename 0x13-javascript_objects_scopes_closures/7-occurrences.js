#!/usr/bin/node
exports.nbOccurences = function (list, thing) {
  const j = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === thing) {
      i++;
    }
  }
  return j;
};
