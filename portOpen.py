import os
import tornado.ioloop
import tornado.web
import json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.set_header('Content-Type', "application/json")
        self.write(json.dumps({"status": "ok"}, indent=2))

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler)
    ])

if __name__ == "__main__":
    try: port = int(input("테스트할 포트 번호 입력 : "))
    except Exception as e: print(f"ERROR! | {e} | 처음부터 다시 입력해주세요!"); exit()
    app = make_app()
    app.listen(port)
    print(f"Server Listen on http://localhost:{port} Port | OS = {'Windows' if os.name == 'nt' else 'UNIX'}")
    os.system(f"start http://localhost:{port}")
    os.system("start https://www.yougetsignal.com/tools/open-ports/")
    tornado.ioloop.IOLoop.current().start()