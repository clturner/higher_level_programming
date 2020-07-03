#!/usr/bin/node
// class Square defines a square and inherits from Rectangle of 4-rectangle.js
const Rectangle = require("./4-rectangle").Rectangle;
function Square (s) {
  Rectangle.call(this, s, s);
};
module.exports.Square = Square;
