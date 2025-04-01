import http.server
import urllib
import re


class OurHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "":
            self.wfile.write(open("main.html", "rb").read())
        else:
            try:
                id = int(self.path[1:])
                open("new_file", "w").write(f"""
                    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="велосипед{id}.jpg"></a>
                    <h1> Самый пиздый таухенный роскошный великолепный превосходный велосипед в вашей жизни</h1>
                    <h2> я сам писал качество гарантирую</h2>
                    <h3> отправьте деньги на номер 89107367465 сбер а мы решим досточно ли вы оплатили за велосипед</h3>
                    <h4> ну и запооните форму ниде с адресом чтобы знать куда оиправлять</h4>
                    """)
                self.wfile.write(
                    open("new_file", "rb").read()
                )
            except Exception as e:
                print("вы ёбгудтсд")
                try:
                    self.wfile.write(open(urllib.parse.unquote(self.path[1:], encoding='utf-8'), "rb").read())
                except Exception as e:
                    print("пошёл нахуй", e)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.wfile.write(post_data)
        print(post_data)


server = http.server.HTTPServer(("localhost", 80), OurHandler)
server.serve_forever()
