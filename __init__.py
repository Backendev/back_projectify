from aplication import Aplication
import argparse

class Endpoint:

    
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Servir aplicacion')
        self.parser.add_argument('-p', '--port', type=int, help='Port aplication server')
        self.args = self.parser.parse_args()
        self.port = 3000
        if self.args.port != None:
            self.port = self.args.port
        a = Aplication(port=self.port)
        a.run_app()


if __name__ == '__main__':
    Endpoint()
    