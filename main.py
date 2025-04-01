import http.server


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return b"Hello world"


server = http.server.HTTPServer(("localhost", 8000), http.server.SimpleHTTPRequestHandler)
server.serve_forever()
