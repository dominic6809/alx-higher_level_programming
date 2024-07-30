#!/usr/bin/node
/**
 * Script that computes the number of tasks completed by user ID.
 * The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
 * Only print users with completed tasks.
 * Module used: request
 */
const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const todos = JSON.parse(body);
    const completedTasksByUser = {};

    todos.forEach((todo) => {
      if (todo.completed) {
        if (completedTasksByUser[todo.userId]) {
          completedTasksByUser[todo.userId]++;
        } else {
          completedTasksByUser[todo.userId] = 1;
        }
      }
    });

    console.log(completedTasksByUser);
  }
});
