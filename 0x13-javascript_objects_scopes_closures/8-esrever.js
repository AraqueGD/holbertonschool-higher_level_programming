#!/usr/bin/node
// Write a function that returns the reversed version of a list:
exports.esrever = function (list) {
  const new_list = [];
  for (let idx = list.length - 1; idx >= 0; idx--) {
    new_list.push(list[idx]);
  }
  return new_list;
};
