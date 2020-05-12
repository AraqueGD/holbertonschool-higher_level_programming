#!/usr/bin/node
/* Write a script that display the status code of a GET request.

    - The first argument is the URL to request (GET)
    - The status code must be printed like this: code: <status code>
    - You must use the module request
*/
const request = require('request');
const args = process.argv.slice(2);
request(args[0], function (error,response) {
    if (error) {
        console.error('error:', error);
    } else {
        console.log(`code: ${response.statusCode}`);
    }
});
