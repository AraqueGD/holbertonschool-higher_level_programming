#!/usr/bin/node
// Write a function that prints the number of arguments already printed and the new argument value. (see example below)
let idx = 0
exports.logMe = function (item) {
    console.log(idx + ': ' + item);
    idx += 1;
}
