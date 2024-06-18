#!/usr/bin/node

/*
function that converts a number from base 10 to another base passed as argument:
Prototype: exports.converter = function (base)
*/
exports.converter = function (base) {
  return function (myNumber) {
    return myNumber.toString(base);
  };
};
