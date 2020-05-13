#!/usr/bin/node
/* Write a script that prints the number of movies where the character “Wedge Antilles” is present.

    - The first argument is the API URL of the Star wars API: https://swapi-api.hbtn.io/api/films/
    - Wedge Antilles is character ID 18
    - You must use the module request
*/
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const id = '18';
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const json = JSON.parse(body);
    for (const i of json.results) {
      for (const film of i.characters) {
        if (film.search(id) > 0) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
