#!/usr/bin/node
/* Write a script that gets the contents of a webpage and stores it in a file.

    - The first argument is the URL to request
    - The second argument the file path to store the body response
    - The file must be UTF-8 encoded
    - You must use the module request
*/
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
const dict = {};
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const json = JSON.parse(body);
    for (const id of json) {
      if (id.completed === true) {
        if (dict[id.userId] === undefined) {
          dict[id.userId] = 0;
        }
        dict[id.userId] += 1;
      }
    }
    console.log(dict);
  }
});
