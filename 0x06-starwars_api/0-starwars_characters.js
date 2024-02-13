#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
if (!movieId || isNaN(movieId)){
    console.error('Usage: ./0-starwars_characters.js <movie_id>');
    process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
      process.exit(1);
    }
    
    if (response.statusCode !== 200) {
      console.error('Invalid response:', response.statusCode);
      process.exit(1);
    }
    
    const filmData = JSON.parse(body);
    
    if (!filmData.characters || filmData.characters.length === 0) {
      console.error('No characters found for this movie.');
      process.exit(1);
    }
    
    const charactersUrls = filmData.characters;
    const charactersPromises = charactersUrls.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
    });
    
    Promise.all(charactersPromises)
      .then((characterNames) => {
        characterNames.forEach((name) => {
          console.log(name);
        });
      })
      .catch((error) => {
        console.error('Error:', error);
        process.exit(1);
      });
  });