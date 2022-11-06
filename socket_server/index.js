const cors = require('cors');
const express = require('express');
const app = express();
app.use(cors())
const http = require('http').Server(app);
const io = require('socket.io')(http, {
  cors: {
    origin: '*',
  }
});
const port = process.env.PORT || 3500;


app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  socket.on('chat message', msg => {
    io.emit('chat message', msg);
  });
  socket.on('retrigger-query', context_msg => {
    console.log('server has received instructions', context_msg)
    io.emit('retrigger-query', context_msg);
  });
});

http.listen(port, () => {
  console.log(`Socket.IO server running at http://127.0.0.1:${port}/`);
});
