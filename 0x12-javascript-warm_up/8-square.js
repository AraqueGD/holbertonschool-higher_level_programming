#!/usr/bin/node
// Write a script that prints a square
const size = parseInt(process.argv.slice(2));

if ((isNaN(size))) {
  console.log('Missing size');
}
for (let idx = 0; idx < size; idx++) {
  console.log('X'.repeat(size));
}
