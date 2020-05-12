#!/usr/bin/node
/* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.

    - The first argument is the movie ID
    - You must use the Star wars API with the endpoint https://swapi-api.hbtn.io/api/films/:id
    - You must use the module request
*/
const request = require('request');
const args = process.argv.slice(2);
const url = 'https://swapi-api.hbtn.io/api/films/' + args[0] + '/';
request(url, function (error, response, body) {
  if (error === null) {
    const json = JSON.parse(body);
    console.log(json.title);
  } else {
    console.error(error);
  }
});
