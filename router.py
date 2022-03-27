from logging import exception
from flask import Flask, request
import json
from data import Data
from g_token import TokenGen
from functools import wraps

class Routers:
    
    def __init__(self,app):
        self.token = False
        self.tg = TokenGen()
        self.d = Data()
        
        @app.route('/login',methods=['POST'])
        def login():
            self.tg.change_secret()
            res_data = request.args.to_dict()
            # res_data = res_data["data"]
            #res_data = json.loads(res_data)
            user = res_data['user']
            passd = res_data['pass']
            res = self.d.get_user(user,passd)
            result = "False"
            if res != None:
                message = {res[1]:res[0]['user']}
                print(message)
                token = self.tg.gen_token(message)
                result = self.tg.get_token()
            return result
        
        @app.route('/verify',methods=['POST'])
        @self.verify_token
        def verify(user):
            res = "yes"
            return res

        @app.route('/new_project',methods=['POST'])
        @self.verify_token
        def new_project(user):
            print("44")
            print(user)
            res_data = request.args.to_dict()
            start = res_data["start"]
            end = res_data["end"]
            name = res_data["name"]
            print(f'Name {name} - Start {start} - End {end}')
            self.d.new_project(start,end,name)
            return "yes"

        @app.route('/new_report',methods=['POST'])
        @self.verify_token
        def new_report(user):
            print("44")
            print(user)
            res_data = request.args.to_dict()
            porcent = res_data["porcent"]
            week = res_data["week"]
            name = res_data["name"]
            self.d.new_report("2",str(name),str(week),str(porcent))
            return "yes"



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
                return fun(result)
            except Exception as e:
                result = "Error"
                return str(e)
                
        return verifing
        