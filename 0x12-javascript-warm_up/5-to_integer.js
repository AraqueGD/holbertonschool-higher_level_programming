#!/usr/bin/node
// Print Number coberted to Integer argument.
const args = process.argv.slice(2);

const number = parseInt(args[0]);

if ((Number.isNaN(number))) {
  console.log('Not a Number');
} else {
  console.log('My number: ' + number);
}
