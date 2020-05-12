#!/usr/bin/node
/* Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

    - You must use the class notation for defining your class and extends
    - Create an instance method called charPrint(c) that prints the rectangle using the character c
        -If c is undefined, use the character X
*/
const Square5 = require('./5-square');
class Square extends Square5 {
  charPrint (c) {
    if (typeof (c) === 'undefined') {
      c = 'X';
    }
    for (let idx = 0; idx < this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
