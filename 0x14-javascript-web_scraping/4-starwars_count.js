#!/usr/bin/node
/**
 * Script that prints the number of movies where the character “Wedge Antilles” is present.
 * The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
 * Wedge Antilles is character ID 18 - script must use this ID for filtering the result of the API.
 * Module used: request
 */
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const films = JSON.parse(body).results;
    const moviesWithWedgeAntilles = films.filter((film) =>
      film.characters.some((character) => character.endsWith(`/${characterId}/`))
    );
    console.log(moviesWithWedgeAntilles.length);
  }
});
