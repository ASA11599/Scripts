const net = require("net");

const HOST = "0.0.0.0";
const PORT = 8080;

const server = net.createServer();

server.on("connection", (s) => {
    s.on("data", (data) => {
        s.write(data);
        if (data.toString().trim() === "exit") {
            s.end();
        } else if (data.toString().trim() === "destroy") {
            s.end();
            server.close();
        }
    });
});

server.listen(PORT, HOST);
