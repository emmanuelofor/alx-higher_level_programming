#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = {};
    for (let i = 0; i < todos.length; i++) {
      const todo = todos[i];
      if (todo.completed) {
        if (completedTasks.hasOwnProperty(todo.userId)) {
          completedTasks[todo.userId] += 1;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    }
    for (const userId in completedTasks) {
      if (completedTasks[userId] === 0) {
        delete completedTasks[userId];
      }
    }
    console.log(completedTasks);
  }
});
