#!/usr/bin/node
// reads and prints contents of a file

const fs = require('fs');

// getting the filepath from command line arguments
const filepath = process.argv[2];

// funtion to read the file
function readFile (path) {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }
  });
}
// calling the function with the filepath
readFile(filepath);
