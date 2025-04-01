import http.server


class OurHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.wfile.write(open("main.html", "rb").read())
        else:
            try:
                self.wfile.write(open(self.path[1:], "rb").read())
            except Exception as e:
                print("пошёл нахуй", e)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.wfile.write(post_data)
        print(post_data)


server = http.server.HTTPServer(("localhost", 80), OurHandler)
server.serve_forever()
