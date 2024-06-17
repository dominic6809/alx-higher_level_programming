#!/usr/bin/node
/* Retrieve the command-line arguments, excluding the first two (node and script path) */
const argsNum = process.argv.slice(2);

/* Check the number of arguments and print the corresponding message */
if (argsNum.length === 0) {
    console.log("No argument");
} else if (argsNum.length === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}
