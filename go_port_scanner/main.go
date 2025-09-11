package main
import (
    "fmt"
    "net"
    "time"
)

func main() {
    host := "127.0.0.1"
    for port := 20; port <= 1024; port++ {
        addr := fmt.Sprintf("%s:%d", host, port)
        conn, err := net.DialTimeout("tcp", addr, 200*time.Millisecond)
        if err == nil {
            fmt.Printf("OPEN: %d\n", port)
            conn.Close()
        }
    }
}