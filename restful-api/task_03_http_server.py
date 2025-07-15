#!/usr/bin/env python3
import json
from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Request handler that supports /, /data, /status, and returns 404 for others."""

    def do_GET(self):
        if self.path == '/':
            # Root endpoint: plain-text greeting
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            # JSON data endpoint
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            payload = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(payload).encode('utf-8'))
        elif self.path == '/status':
            # Health-check endpoint
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"OK")
        elif self.path == '/info/':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode('utf-8'))
        else:
            # Undefined endpoint → 404
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            message = f"Endpoint not found"
            self.wfile.write(message.encode('utf-8'))


def run_server(host: str = '0.0.0.0', port: int = 8000) -> None:
    """Start the HTTP server."""
    server_address = (host, port)
    httpd = HTTPServer(server_address, SimpleAPIHandler)
    print(f'Serving on http://{host}:{port}')
    httpd.serve_forever()


if __name__ == '__main__':
    run_server()
