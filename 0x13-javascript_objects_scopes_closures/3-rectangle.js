#!/usr/bin/node

/*
class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
*/
class Rectangle {
  constructor (w, h) {
    if (
      w <= 0 ||
      h <= 0 ||
      typeof w !== 'number' ||
      typeof h !== 'number' ||
      !Number.isInteger(w) ||
      !Number.isInteger(h)
    ) {
      return {};
    }
    this.width = w;
    this.height = h;
  }

  // Instance method print() that prints the rectangle using the character X
  print () {
    if (!this.width || !this.height) {
      console.log('Invalid dimensions for the rectangle.');
      return;
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}