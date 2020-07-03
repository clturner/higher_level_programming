#!/usr/bin/node
// function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
  let reversed_list = [];
  let length = list.length;
  let count = 0;
  for (let x of list) {
  reversed_list.push(x);
  reversed_list.reverse();
  }
  for (let x = 0; x < length; x++) {
    if (reversed_list[x] == searchElement) {
      count += 1;
    }
  };
  return(count);
};
