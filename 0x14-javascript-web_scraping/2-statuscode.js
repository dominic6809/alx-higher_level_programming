#!/usr/bin/node
/**
 * Script that displays the status code of a GET request.
 * The first argument is the URL to request (GET).
 * The status code must be printed like this: code: <status code>.
 * Module used: request
 */

const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error(`Error ${error}`);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
