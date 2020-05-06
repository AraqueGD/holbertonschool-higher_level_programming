#!/usr/bin/node
// Write a script that computes and prints a factorial.
function factorialRecursivo (n) {
  if (isNaN(n) || n === 1) {
    return 1;
  }
  return n * factorialRecursivo(n - 1);
}
console.log(factorialRecursivo(parseInt(process.argv[2])));
