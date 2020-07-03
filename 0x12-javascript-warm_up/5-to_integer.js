#!/usr/bin/node
// check if argument is an integer
const arg = parseInt(process.argv[2]);
if (Number.isNaN(arg) == true) {
    console.log('Not a number');
} else {
    console.log('My number:', arg);
}
