#!/usr/bin/node

// Get the first argument passed to the script
const args = process.argv[2];

// Convert the argument to an integer
const sizeInt = parseInt(args);

// Check if the conversion is successful and the size is a positive integer
if (!isNaN(sizeInt) && sizeInt > 0) {
  for (let i = 0; i < sizeInt; i++) {
    const line = 'X'.repeat(sizeInt);
    console.log(line);
  }
} else {
  console.log('Missing size');
}
