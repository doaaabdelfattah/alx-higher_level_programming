#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const completed = {};
    data.forEach(task => {
      if (task.completed) {
        completed[task.userId] = (completed[task.userId] || 0) + 1;
      }
    });
    console.log(completed);
  }
});
