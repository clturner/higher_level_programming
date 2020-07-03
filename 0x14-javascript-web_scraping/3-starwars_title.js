#!/usr/bin/node
// prints the title of a Star Wars movie matches argv[2] with episode #
const request = require('request');
url = "http://swapi.co/api/films/" + process.argv[2]
request(url, function(err, res, body) {
  console.log(JSON.parse(body).title);
});
