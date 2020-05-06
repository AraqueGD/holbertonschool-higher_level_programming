#!/usr/bin/node
// Write a script that prints two arguments passed to it, in the following format: “ is ”
const args = process.argv.slice(2);

const one = args[0];
const two = args[1];

if ((!one)) {
  console.log(one + ' is ' + two);
} else if ((one.length === 1)) {
  console.log(one + ' is ' + two);
} else {
  console.log(one + ' is ' + two);
}
