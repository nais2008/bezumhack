import http.server


class OurHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.wfile.write(open("main.html", "rb").read())

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.wfile.write(post_data)
        print(post_data)


server = http.server.HTTPServer(("localhost", 80), OurHandler)
server.serve_forever()
