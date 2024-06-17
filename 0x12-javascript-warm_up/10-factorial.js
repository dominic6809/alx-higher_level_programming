#!/usr/bin/node

// Define a recursive function to compute factorial
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (isNaN(n) || n < 0) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    // Recursive case: n * factorial(n-1)
    return n * factorial(n - 1);
  }
}

// Get the first argument passed to the script
const arg = process.argv[2];

const numInt = parseInt(arg);

// Calculate the factorial using the factorial function
const result = factorial(numInt);

console.log(result);
