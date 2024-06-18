#!/usr/bin/node
/* script that imports an array and computes a new array. */

const { arr } = require('./100-data');

const newList = arr.map((value, index) => value * index);

console.log(arr);
console.log(newList);

