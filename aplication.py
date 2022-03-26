from flask import Flask, request
from router import Routers


class Aplication:
    def __init__(self,port):
        self.app = Flask(__name__)
        self.port = port
        self.router()
    def router(self):
        Routers(self.app)
    def run_app(self):
        self.app.run(host='0.0.0.0', port=self.port)