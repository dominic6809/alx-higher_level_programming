#!/usr/bin/node
/**
 * prints the title of a Star Wars movie where the episode number matches a given integer.
 * The first argument is the movie ID.
 * Uses the Star Wars API with the endpoint https://swapi-api.alx-tools.com/api/films/:id.
 * Module used: request
 */

const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the API endpoint URL with the provided movie ID
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Send a GET request using the 'request' module
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
  } else if (response.statusCode !== 200) {
    console.error(`Error: Unexpected status code ${response.statusCode}`);
  } else {
    const movieDetails = JSON.parse(body);

    console.log(movieDetails.title);
  }
});
