#!/usr/bin/node

/*
function that returns the number of occurrences in a list:

Prototype: exports.nbOccurences = function (list, searchElement)
*/
exports.nbOccurences = function (list, searchElement) {
  let countNumber = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      countNumber++;
    }
  }
  return countNumber;
};
