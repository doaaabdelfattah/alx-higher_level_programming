#!/usr/bin/node


const fs = require('fs');
// Get the file path from command-line arguments
const filePath = process.argv[2];

// Asynchronous method
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});