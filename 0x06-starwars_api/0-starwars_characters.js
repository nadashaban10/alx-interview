#!/usr/bin/node
const request = require('request');

// Function to fetch and print character names by movie ID
function printStarWarsCharacters(movieId) {
  const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

  // Fetch the movie details
  request(apiUrl, { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }
    if (!body || !body.characters) {
      console.log('No characters found for this movie.');
      return;
    }

    // Iterate through the characters list
    body.characters.forEach((characterUrl) => {
      // Fetch each character's details
      request(characterUrl, { json: true }, (charErr, charRes, charBody) => {
        if (charErr) { return console.log(charErr); }
        // Print the character's name
        console.log(charBody.name);
      });
    });
  });
}

// Get the movie ID from the first positional argument
const movieId = process.argv[2];

// Validate the movie ID
if (!movieId) {
  console.log('Please provide a Movie ID as the first positional argument.');
} else {
  printStarWarsCharacters(movieId);
}
