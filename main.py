import http.server
import urllib
import random




class OurHandler(http.server.BaseHTTPRequestHandler):
    счётчик = 0
    def do_GET(self):
        OurHandler.счётчик += 1
        if OurHandler.счётчик % 5 == 0 and self.path in ["/", "/admin", ""]:
            print("греем гоев")
            self.wfile.write(b"site deadinside. skinte dengi mb voskresnet 89107367465")
            return
        if self.path == "/" or self.path == "":
            self.wfile.write(open("main.html", "rb").read())
        elif self.path == "/admin":
            open("new_file", "w").write(
                """
                <a href="/stopserver">stopserver</a>
                """
            )
            self.wfile.write(open("new_file", "rb").read())
        elif self.path == "/stopserver":
            self.wfile.write(b"server closed")
            exit(0)
        elif self.path == "/submitorderform":
            open("new_file", "w").write(
                """
                <h1>Нам насрать на ваши данные. Заполните сами</h1>
                <audio autoplay="autoplay">
                    <source src="важный_звонок.mp3" type="audio/mp3">
                </audio>

                <img src="obezmyana.jpg">
                <h1>
                <a href="https://1drv.ms/x/c/f848ae55d97bc4d8/EfdC70As3bdJiUxvCvOBkZ8B8b_MghAeoYkjwG34bxiExA?e=GzbnBY">
                https://1drv.ms/x/c/f848ae55d97bc4d8/EfdC70As3bdJiUxvCvOBkZ8B8b_MghAeoYkjwG34bxiExA?e=GzbnBY
                </a>
                </h1>
                
                """
            )
            self.wfile.write(open("new_file", "rb").read())
        else:
            try:
                id = int(self.path[1:])
                opisanie = "Самый пиздый таухенный роскошный великолепный превосходный велосипед в вашей жизни".split()
                random.shuffle(opisanie)
                opisanie = " ".join(opisanie)
                open("new_file", "w").write(f"""
                <head>
    <link rel="icon" type="image/x-icon" href="/favicon.png">
    <meta name="description" content="Магазин велосипедов с анимированным карусельным отображением">
    <meta name="keywords" content="велосипеды, магазин, спорт, активный отдых">
    <title>Магазин велосипедов</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Shafarik&display=swap" rel="stylesheet">
    <style>
        *{'''{
                font-family: "Shafarik", system-ui;
            font-weight: 400;
            font-style: normal;}
        '''
                }
    </style>
    </head>
    <body>
                    <a href="/"> open the door </a>
                    <a href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"><img src="велосипед{random.randint(1, 14)}.jpg"></a>
                    <h1>{opisanie}</h1>
                    <h2> я сам писал качество гарантирую</h2>
                    <h3> отправьте деньги на номер 89107367465 сбер а мы решим досточно ли вы оплатили за велосипед</h3>
                    <h4> ну и запооните форму ниде с адресом чтобы знать куда оиправлять</h4>
                    <form method="POST" enctype="application/json">
                        <input name="name" value="name" >
                        <input name="lastname" value="lastname" >
                        <input name="lastlastname" value="lastlastname" >
                        <input name="address" value="сука где ты дивёшь" >
                        <input name="telephone" type="tel" value="твой телефон сука">
                        <input name="monet" type="number" value="сколько ты скинул">
                        <button type="submit"> click me</button>
                    </form>
                    <iframe width=50% height=50% src="https://1drv.ms/x/c/f848ae55d97bc4d8/EfdC70As3bdJiUxvCvOBkZ8B8b_MghAeoYkjwG34bxiExA?e=GzbnBY">
                    </iframe>
                    <audio controls src="Научно-технический%20рэп%20-%20Костыль%20и%20велосипед.mp3" type="audio/mp3" id="audio">Извините но это
        мы
    </audio>
    <a href="https://1drv.ms/x/c/f848ae55d97bc4d8/EfdC70As3bdJiUxvCvOBkZ8B8b_MghAeoYkjwG34bxiExA?e=GzbnBY">если идёте нахуй то сюда</a>
                    <script>
                    audio = document.getElementById("audio");
    var first = true;
    document.onclick = function () {'''{
        if (first == true) audio.play()
        first = false;}'''
                }
                    </script>
                    </body>
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
        self.wfile.write(b"<p>")
        self.wfile.write(post_data)
        self.wfile.write(
            b"\nvashe obraschenie razzmatrivaetsya</p><script>setTimeout(() => {window.location.replace('/submitorderform')}, 200)</script>")
        open("база даннных/" + str(random.random().__hash__()), "wb").write(post_data)


import asyncio


async def s1():
    server = http.server.HTTPServer(("localhost", 80), OurHandler)
    server.serve_forever()


async def s2():
    server2 = http.server.HTTPServer(("localhost", 1237), http.server.BaseHTTPRequestHandler)
    server2.serve_forever()


asyncio.run(s1())
asyncio.run(s2())
