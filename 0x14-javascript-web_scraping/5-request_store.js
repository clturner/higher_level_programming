#!/usr/bin/node
//  script that gets the contents of a webpage and stores it in a file
const request = require('request');
request(process.argv[2], function(err, res, body) {
  const fs = require('fs');
  fs.writeFile(process.argv[3], body, 'utf8', (err) => {});
});
