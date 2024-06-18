#!/usr/bin/node

const fs = require('fs');

const newArgs = fs.readFileSync(process.argv[2]).toString();
const oldArgs = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], newArgs + oldArgs);
