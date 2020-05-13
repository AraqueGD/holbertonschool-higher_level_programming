#!/usr/bin/node
/* Write a script that gets the contents of a webpage and stores it in a file.

    - The first argument is the URL to request
    - The second argument the file path to store the body response
    - The file must be UTF-8 encoded
    - You must use the module request
*/
const fs = require('fs');
const request = require('request');
const args = process.argv.slice(2);
const url = args[0];
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    fs.writeFileSync(args[1], body, 'utf-8', { flag: 'w+' });
  }
});
