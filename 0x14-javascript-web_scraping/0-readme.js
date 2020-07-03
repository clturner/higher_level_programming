#!/usr/bin/node
// print txt from a file
var fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function(err, data) {
  if (err) throw err;
    process.stdout.write(data);
});
