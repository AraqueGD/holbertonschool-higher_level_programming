#!/usr/bin/node
// Write a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dic = require('./101-data').dict;
const newDict = {};
Object.keys(dic).map(function (key, index) {
  if (newDict[dic[key]] === undefined) {
    newDict[dic[key]] = [];
  }
  newDict[dic[key]].push(key);
});
console.log(newDict);
