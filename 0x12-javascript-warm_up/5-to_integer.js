#!/usr/bin/node
const args = process.argv[2];

// Convert the argument to an integer
const number = parseInt(args, 10);

// Check if the conversion is successful
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
