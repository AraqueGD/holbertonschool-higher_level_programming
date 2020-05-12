#!/usr/bin/node
/* Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

    - You must use the class notation for defining your class and extends
    - Create an instance method called charPrint(c) that prints the rectangle using the character c
        -If c is undefined, use the character X
*/
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let idx = 0; idx < this.height; idx++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const save = this.width;
    this.width = this.height;
    this.height = save;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let idx = 0; idx < this.height; idx++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
