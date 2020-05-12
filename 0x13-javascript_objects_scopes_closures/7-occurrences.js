#!/usr/bin/node
// Write a function that returns the number of occurrences in a list:
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  let found;
  for (found in list) {
    if (list[found] === searchElement) {
      count += 1;
    }
  }
  return (count);
};
