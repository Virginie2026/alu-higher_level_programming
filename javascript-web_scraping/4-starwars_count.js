#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    const count = films.reduce((acc, film) => {
      const hasWedge = film.characters.some((character) => character.endsWith('/18/'));
      return hasWedge ? acc + 1 : acc;
    }, 0);
    console.log(count);
  }
});
