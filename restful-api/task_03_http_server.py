#!/usr/bin/env python3
import json
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json; charset=utf-8')
            self.end_headers()
            payload = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(payload).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            message = f"404 Not Found: The requested URL {self.path} was not found on this server."
            self.wfile.write(message.encode('utf-8'))


def run_server(host: str = '0.0.0.0', port: int = 8000) -> None:
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f"Serving on http://{host}:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
