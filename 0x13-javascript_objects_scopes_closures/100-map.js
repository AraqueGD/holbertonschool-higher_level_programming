#!/usr/bin/node
// Write a script that imports an array and computes a new array.
const list = require('./100-data');
const map1 = list.map(function(num, index){
    return (num * index);
});
console.log(list);
console.log(map1);
