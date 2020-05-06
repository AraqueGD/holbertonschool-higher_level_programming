#!/usr/bin/node
// Write a script that prints the addition of 2 integers.
const args = process.argv.slice(2);
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}
add(args[0], args[1]);
