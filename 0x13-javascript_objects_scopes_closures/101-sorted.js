#!/usr/bin/node

/*
script that imports a dictionary of occurrences by user id
and computes a dictionary of user ids by occurrence.
*/
const dict = require('./101-data').dict;

const newlist = Object.entries(dict);
const vals = Object.values(dict);
const uniqVals = [...new Set(vals)];
const newDict = {};
for (const j in uniqVals) {
  const list = [];
  for (const k in newlist) {
    if (newlist[k][1] === uniqVals[j]) {
      list.unshift(newlist[k][0]);
    }
  }
  newDict[uniqVals[j]] = list;
}
console.log(newDict);
