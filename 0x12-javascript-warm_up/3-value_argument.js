#!/usr/bin/node
// script that checks for argumnets
if (process.argv.slice(2) == '') {
    console.log('No argument');
} else {
    console.log(process.argv[2]);
}
