from argparse import ArgumentParser

from flask import Flask
from config import DevConfig

# 初始化 Flask 類別成為 instance
app = Flask(__name__)
app.config.from_object(DevConfig)

# 路由和處理函式配對
@app.route('/')
def index():
    return 'Hello World!'

# 判斷自己執行非被當做引入的模組，因為 __name__ 這變數若被當做模組引入使用就不會是 __main__
if __name__ == '__main__':

    # arg_parser = ArgumentParser(
    #     usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    # )
    # arg_parser.add_argument('-p', '--port', default=1299, help='port')
    # arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    # arg_parser.add_argument('--host', default="192.168.1.151", help='set host location')
    #
    # options = arg_parser.parse_args()
    #
    # app.run(host=options.host, debug=options.debug, port=options.port);
    app.run(host='192.168.1.151', port=2988, debug=True)
    # app.run()