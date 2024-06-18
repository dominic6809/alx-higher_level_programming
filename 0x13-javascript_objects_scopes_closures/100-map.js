#!/usr/bin/node

/* script that imports an array and computes a new array. */
const lst = require('./100-data').list;

console.log(lst);
console.log(lst.map((x, idx) => x * idx));

