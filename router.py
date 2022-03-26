from flask import Flask, request
import json
from data import Data
from g_token import TokenGen
from functools import wraps

class Routers:
    
    def __init__(self,app):
        self.token = False
        self.tg = TokenGen()
        @app.route('/login',methods=['POST'])
        def login():
            self.tg.change_secret()
            res_data = request.args.to_dict()
            res_data = res_data["data"]
            res_data = json.loads(res_data)
            print(res_data['user'])
            d = Data()
            res = d.get_user(res_data['user'],res_data['pass'])
            print(f'GGGG {res}')
            result = "False"
            if res != None:
                message = {res[1]:res[0]['user']}
                print(message)
                token = self.tg.gen_token(message)
                result = self.tg.get_token()
            return result
        
        @app.route('/verify',methods=['POST'])
        @self.verify_token
        def verify():
            res = "yes"
            return res

    def verify_token(self,fun):
        @wraps(fun)
        def verifing(*args,**kwargs):
            auth_headers = request.headers.get('Authorization', '').split()
            print(auth_headers)
            token = auth_headers[1]
            result = "False"
            try:
                result = self.tg.get_desc_token(token)
                print(f'Resulttok {result}')
                self.token = True
                return fun()
            except:
                result = "Error"
                return "Error"
                
        return verifing
        