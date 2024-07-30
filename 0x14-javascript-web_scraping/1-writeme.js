#!/usr/bin/node
/**
 * script that writes a string to a file
 * file path
 * string to write
 * content to be written in 'utf-8'
 * print error object incase of error
 */
const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
  if (err) {
    console.error(err);
  }
});
