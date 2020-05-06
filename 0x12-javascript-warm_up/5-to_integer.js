#!/usr/bin/node
// Print Number coberted to Integer argument.
const number = parseInt(process.argv.slice(2));

if ((Number.isNaN(number))) {
  console.log('Not a Number');
} else if ((typeof number === 'number')){
  console.log('My number: ' + number);
}
