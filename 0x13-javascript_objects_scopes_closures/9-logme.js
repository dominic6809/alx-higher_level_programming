#!/usr/bin/node

/*
function that prints the number of arguments already printed and the new argument value.
Prototype: exports.logMe = function (item)
Output format: <number arguments already printed>: <current argument value>
 */
let countNo = 0;

exports.logMe = function (item) {
  console.log(`${countNo}: ${item}`);
  countNo++;
};
