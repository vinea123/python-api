from http.server import BaseHTTPRequestHandler
from controller.welcome import welcome_handler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # welcome.py
    ROUTES_GET = { "/": welcome_handler }
    ROUTES_POST = {"/": welcome_handler}
    ROUTES_PUT = {"/": welcome_handler}
    ROUTES_DELETE = {"/": welcome_handler}

    def handle_request(self, method_routes):
        handler = method_routes.get(self.path)
        if handler:
            status, headers, body = handler()
        else:
            status = 404
            headers = {"Content-Type": "application/json"}
            body = b'{"error": "Not Found"}'

        self.send_response(status)
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self.handle_request(self.ROUTES_GET)

    def do_POST(self):
        self.handle_request(self.ROUTES_POST)

    def do_PUT(self):
        self.handle_request(self.ROUTES_PUT)

    def do_DELETE(self):
        self.handle_request(self.ROUTES_DELETE)
