#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function (list) {
  let reversed_list = [];
  let length = list.length;
  for (let x of list) {
    reversed_list.push(x);
    reversed_list.reverse();
  }
  return(reversed_list);
};
