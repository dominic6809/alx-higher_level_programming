#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie based on the given Movie ID.
 * The first argument is the Movie ID.
 * Display one character name by line.
 * Module used: request
 */
const request = require('request');
const starWarsID = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(starWarsID, function (error, response, body) {
  if (error) {
    console.error('Error fetching movie details:', error);
    return;
  }

  try {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    if (!characters || characters.length === 0) {
      console.log('No characters found for this movie.');
      return;
    }

    characters.forEach((characterURL) => {
      request(characterURL, function (charError, charResponse, charBody) {
        if (charError) {
          console.error('Error fetching character details:', charError);
        } else {
          const characterData = JSON.parse(charBody);
          console.log(characterData.name);
        }
      });
    });
  } catch (parseError) {
    console.error('Error parsing JSON:', parseError);
  }
});
