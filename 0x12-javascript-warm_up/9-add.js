#!/usr/bin/node
// adds two args
function add (a, b) {
  return parseInt(a) + parseInt(b);
}

const num = add(process.argv[2], process.argv[3]);
console.log(num);
