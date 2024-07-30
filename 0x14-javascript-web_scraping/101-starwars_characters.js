#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie based on the given Movie ID.
 * The first argument is the Movie ID.
 * Display one character name by line, following the order from the /films/ response.
 * Module used: request
 */
const request = require('request');

function fetchData (url) {
  return new Promise((resolve, reject) => {
    request(url, (err, _res, body) => {
      if (err) {
        reject(err);
      } else {
        resolve(body);
      }
    });
  });
}

function printMovieCharacters (movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  fetchData(movieUrl)
    .then((movieData) => {
      const movie = JSON.parse(movieData);
      const characterUrls = movie.characters;
      const characterPromises = characterUrls.map((characterUrl) => fetchData(characterUrl));

      return Promise.all(characterPromises);
    })
    .then((charactersData) => {
      charactersData.forEach((characterData) => {
        const character = JSON.parse(characterData);
        console.log(character.name);
      });
    })
    .catch((err) => {
      console.error('Error:', err);
    });
}

const selectedMovieId = process.argv[2];
printMovieCharacters(selectedMovieId);
