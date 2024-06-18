#!/usr/bin/node
/* 
class Square that defines a square and inherits from Square of 5-square.js:
*/
const SquareS = require('./5-square');

class Square extends SquareS {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      let r = '';
      for (let j = 0; j < this.width; j++) {
        r += c;
      }
      console.log(r);
    }
  }
}

module.exports = Square;
