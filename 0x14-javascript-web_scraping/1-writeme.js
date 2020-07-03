#!/usr/bin/node
// script that writes a string to a file.
var fs = require('fs');
fs.writeFile(process.argv[2], process.argv[3], 'utf8', (err) => {
  if (err) throw err;
  console.log('The file has been saved!');
});
