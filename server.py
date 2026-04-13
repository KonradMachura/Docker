# server.py — a minimal HTTP server that listens for incoming requests

from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send a 200 OK status back to whoever called us
        self.send_response(200)
        self.end_headers()
        # Write the response body as bytes
        self.wfile.write(b"Hello from the server container!")

    def log_message(self, format, *args):
        # Override to print a cleaner log line
        print(f"[server] request from {self.client_address[0]}: {args[0]}")

# "0.0.0.0" means "listen on all network interfaces inside the container"
# so Docker can route traffic to it from other containers
HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
