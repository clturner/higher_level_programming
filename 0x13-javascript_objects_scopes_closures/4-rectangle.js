#!/usr/bin/node
// Write a class Rectangle that defines a rectangle
function Rectangle (w, h) {
  if (w <= 0 || h <= 0 ) {
    return;
  } else if (typeof w == 'undefined') {
    return;
  } else if (typeof h == 'undefined') {
    return;
  } else {
    this.width = w;
    this.height = h;
    this.print = function () {
      for (let x = 0; x < h; x++) {
        for (let y = 0; y < w; y++) {
          process.stdout.write('X');
        }
        console.log();
      }
    }
    this.double = function () {
      w = w*2;
      h = h*2;
    }
    this.rotate = function () {
      let a = w;
      w = h;
      h = a;
    }
  }
};
module.exports.Rectangle = Rectangle;
