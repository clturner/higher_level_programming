#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present.
const request = require('request');
request(process.argv[2], function(err, res, body) {
  Wedge_id = 18;
  number_Wedge_movies = 0;
  let a = JSON.parse(body).results;
  let count = Object.keys(a).length;
  for (x = 0; x < count; x++) {
    b = a[x]['characters'];
    let count1 = Object.keys(b).length;
    for (y = 0; y < count1; y++) {
      if (b[y].includes(Wedge_id) == true) {
        number_Wedge_movies += 1;
      }
    }
  }
  console.log(number_Wedge_movies);
});
