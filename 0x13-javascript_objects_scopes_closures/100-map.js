#!/usr/bin/node
// Write a script that imports an array and computes a new array.
const list = require('./100-data').list;
const multiIndex = (num, index) => num * index
const map1 = list.map(multiIndex);
console.log(list);
console.log(map1);
