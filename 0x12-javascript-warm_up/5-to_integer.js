#!/usr/bin/node
const args = process.argv.slice(2);

const number = parseInt(args[0], 10);

if ((!number)) {
  console.log('Not a Number');
} else {
  console.log('My number: ' + number);
}
