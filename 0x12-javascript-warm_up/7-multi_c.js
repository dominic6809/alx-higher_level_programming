#!/usr/bin/node

// Get the first argument passed to the script
const args = process.argv[2]

// Convert the argument to an integer
const val = parseInt(args, 10)

// Check if the conversion is successful
if (isNaN(val)) {
  console.log('Missing number of occurrences')
} else {
  for (let i = 0; i < val; i++) {
    console.log('C is fun')
  }
}
