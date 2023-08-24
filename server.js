const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const io = new Server(server);
const axios = require("axios");

app.use(express.json());

app.get("/", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

app.get("/index.html", (req, res) => {
    res.sendFile(__dirname + "/index.html");
});

app.get("/realchat.html", (req, res) => {
    res.sendFile(__dirname + "/realchat.html");
});

app.get("/login.html", (req, res) => {
    res.sendFile(__dirname + "/login.html");
});

app.get("/blog.html", (req, res) => {
    res.sendFile(__dirname + "/blog.html");
});

app.get("/contact.html", (req, res) => {
    res.sendFile(__dirname + "/contact.html");
});

app.post('/submit', (req, res) => {
    const name = req.body.name;
    const email = req.body.email;
    const message = req.body.message;

    res.send('Thank you for your message');
});

app.post('/api/openai', async (req, res) => {
    const prompt = req.body.prompt;

    try {
        // Flaskサーバーへのリクエスト転送
        const response = await axios.post('http://localhost:5000/api/openai', {
            prompt: prompt
        });

        res.json(response.data);

    } catch (error) {
        console.log("Error calling flask server", error.response.data);
        res.status(500).json({ error: 'Failed to get a response from Flask server' });
    }
});

io.on("connection", (socket) => {
    console.log("ユーザーが接続しました");
    socket.on("chat message", (msg) => {
        // console.log("massage:" + msg);
        io.emit("chat message", msg);
    });
});

server.listen(process.env.PORT || 3000, () => {
    console.log("listenin on 3000");
});