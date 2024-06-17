#!/usr/bin/node

// Define the add function
function add(a, b) {
  return a + b;
}

const args1 = process.argv[2];
const args2 = process.argv[3];

// Convert the arguments to integers
const num1 = parseInt(args1);
const num2 = parseInt(args2);

// Check if both arguments are valid integers
if (!isNaN(num1) && !isNaN(num2)) {
  // Function call
  const result = add(num1, num2);
  console.log(result);
} else {
  console.log("NaN");
}
