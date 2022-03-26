from flask import Flask, request
import json


class Aplication:
    def __init__(self,port):
        self.app = Flask(__name__)
        self.port = port
        self.router()
    def router(self):
        @self.app.route('/',methods=['POST'])
        def hello():
            res_data = request.args.to_dict()
            res_data = res_data["data"]
            res_data = json.loads(res_data)
            print(res_data)
            return 'Hello, World!'
    def run_app(self):
        self.app.run(host='0.0.0.0', port=self.port)