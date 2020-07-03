#!/usr/bin/node
// function that converts a number from base 10 to a base passed as argument
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
      console.log(num);
  };
};
