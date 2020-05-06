#!/usr/bin/node
// Write a script that prints x times “C is fun”
const num = parseInt(process.argv.slice(2));

if ((isNaN(num))) {
    console.log('Missing number of occurrences')
}
for (let idx = 0; idx < num; idx++) {
    console.log('C is fun');
}
