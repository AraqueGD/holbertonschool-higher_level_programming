#!/usr/bin/node
// Write a script that prints a message depending of the number of arguments passed.
let args = process.argv

if ((args.length === 2)) {
    console.log('No argument')
} else if ((args.length === 3)) {
    console.log('Argument Found')
} else {
    console.log('Arguments found')
}