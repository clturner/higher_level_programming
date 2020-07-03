#!/usr/bin/node
// script that display the status code of a GET request.
const request = require('request');
request(process.argv[2], function(err, res, body) {
    console.log("code: " + res['statusCode']);
});
