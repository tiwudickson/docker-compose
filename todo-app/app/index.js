const express = require('express');
const mongoose = require('mongoose');

const app = express();
app.use(express.json());

mongoose.connect('mongodb://mongo:27017/todo-app', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const todoSchema = new mongoose.Schema({
  task: String,
});

const Todo = mongoose.model('Todo', todoSchema);

app.get('/todos', async (req, res) => {
  const todos = await Todo.find();
  res.json(todos);
});

app.post('/todos', async (req, res) => {
  const newTodo = new Todo({
    task: req.body.task,
  });
  await newTodo.save();
  res.status(201).json(newTodo);
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
