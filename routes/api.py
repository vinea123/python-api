from http.server import BaseHTTPRequestHandler
from controller.welcome import welcome_handler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    ROUTES = {
        "/": welcome_handler,
    }

    def do_GET(self):
        handler = self.ROUTES.get(self.path)
        if handler:
            status, headers, body = handler()
        else:
            status, headers, body = 404, {"Content-Type": "application/json"}, b'{"error": "Not Found"}'

        self.send_response(status)
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)
