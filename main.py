import http.server


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(open("main.html", "rb").read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.wfile.write(post_data)


server = http.server.HTTPServer(("localhost", 8000), Handler)
server.serve_forever()
