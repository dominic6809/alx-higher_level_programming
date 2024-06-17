#!/usr/bin/node

/* Get the arguments passed to the script
(excluding the first two which are node and script name)
*/
const args = process.argv.slice(2);

// Convert arguments to integers and filter out any NaN values
const numbers = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));

if (numbers.length === 0) {
  console.log(0);
} else if (numbers.length === 1) {
  // If there is only one valid number, print 0
  console.log(0);
} else {
  // Sort numbers in descending order
  numbers.sort((a, b) => b - a);

  const secondBiggest = numbers[1];

  console.log(secondBiggest);
}
