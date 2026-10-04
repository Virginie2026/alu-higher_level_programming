#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const film = JSON.parse(body);
    console.log(film.title);
  }
});
