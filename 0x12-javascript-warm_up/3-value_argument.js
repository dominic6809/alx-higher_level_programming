#!/usr/bin/node
/* Retrieve the command-line arguments,
excluding the first two (node and script path)
Print the first argument if it exists, otherwise print "No argument"
*/
const argsNum = process.argv.slice(2);

console.log(argsNum[0] || "No argument");
