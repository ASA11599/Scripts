package main

import (
	"bytes"
	"fmt"
	"log"
	"net"
)

func logIfError(e error) {
	if e != nil { log.Fatal(e) }
}

type messageHandler func([]byte) []byte

func echo(req []byte) []byte {
	return req
}

func handleConnection(c *net.TCPConn, ending []byte, handler messageHandler) {
	defer c.Close()
	msg := make([]byte, 0)
	for len(msg) < len(ending) || !bytes.HasSuffix(msg, ending) {
		chunk := make([]byte, len(ending))
		br, err := c.Read(chunk)
		logIfError(err)
		msg = append(msg, chunk[:br]...)
	}
	c.Write(handler(msg))
	fmt.Print(string(msg))
}

func serve() {
	listener, err := net.ListenTCP("tcp4", &net.TCPAddr{IP: net.ParseIP("0.0.0.0"), Port: 8080})
	logIfError(err)
	defer listener.Close()
	for i := 0; i < 5; i++ {
		connection, err := listener.AcceptTCP()
		logIfError(err)
		go handleConnection(connection, []byte("\n"), echo)
	}
}

func main() {
	serve()
}
