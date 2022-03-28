from logging import exception
from flask import Flask, request
import json
from data import Data
from data_aux import DataAux
from g_token import TokenGen
from functools import wraps

class Routers:
    def __init__(self,app):
        self.token = False
        self.tg = TokenGen()
        self.d = Data()
        self.da = DataAux()
        self.app = app
        self.error = "No se pudo resolver la solicitud"

        @app.route('/login',methods=['POST'])
        def login():
            self.tg.change_secret()
            request_data = request.args.to_dict()
            list_params = {"user":"text","pass":"text"}
            res,errors = self.da.validate_params(request_data,list_params)
            if len(errors) > 0:
                return self.generate_response(errors,200)
            user = res['user']
            passd = res['pass']
            res = self.d.get_user(user,passd)
            if res != None:
                try:
                    message = {res[1]:res[0]['user']}
                    token = self.tg.gen_token(message)
                    result = self.tg.get_token()
                    return self.generate_response(result,200)
                except:
                    return self.generate_response(self.error,500)
            else:
                return self.generate_response("Usuario o contraseña incorrectos",200)
        

        @app.route('/new_user',methods=['POST'])
        def new_user():
            request_data = request.args.to_dict()
            list_params = {"user":"text","pass":"text"}
            request_data,errors = self.da.validate_params(request_data,list_params)
            if len(errors) > 0:
                return self.generate_response(errors,200)
            try:
                user = request_data['user']
                passd = request_data['pass']
                resp = self.d.new_user(user,passd)
                return self.generate_response(resp,200)
            except:
                return self.generate_response(self.error,500)
        

        @app.route('/verify',methods=['POST'])
        @self.verify_token
        def verify(user):
            print(user)
            user = self.d.get_user_id(user)
            print(user)
            return self.generate_response("Yes",200)


        @app.route('/new_project',methods=['POST'])
        @self.verify_token
        def new_project(user):
            request_data = request.args.to_dict()
            list_params = {"start":"date","end":"date","name":"text"}
            request_data,errors = self.da.validate_params(request_data,list_params)
            if len(errors) > 0:
                return self.generate_response(errors,200)
            try:
                start = request_data["start"]
                end = request_data["end"]
                name = request_data["name"]
                print(f'Name {name} - Start {start} - End {end}')
                response = self.d.new_project(start,end,name)
                return self.generate_response(response,200)
            except:
                return self.generate_response(self.error,500)


        @app.route('/new_report',methods=['POST'])
        @self.verify_token
        def new_report(user):
            request_data = request.args.to_dict()
            list_params = {"porcent":"number","week":"week","name":"text"}
            request_data,errors = self.da.validate_params(request_data,list_params)
            if len(errors) > 0:
                return self.generate_response(errors,200)
            try:
                porcent = request_data["porcent"]
                week = request_data["week"]
                name = request_data["name"]
                self.d.new_report(user,str(name),str(week),str(porcent))
                return self.generate_response("yes",200)
            except:
                return self.generate_response(self.error,500)
        

        @app.route('/reports/<user_name>',methods=['GET'])
        @self.verify_token_p
        def reports_name(user_name):
            list_params = {"user_name":"text"}
            request_data = {"user_name":user_name}
            request_data,errors = self.da.validate_params(request_data,list_params)
            if len(errors) > 0:
                return self.generate_response(errors,200)
            try:
                results = self.d.get_reports(user_name)
                return self.generate_response(results,200,type="json")
            except:
                return self.generate_response(self.error,500)


        @app.route('/my_reports/',methods=['GET'])
        @self.verify_token
        def my_reports(user):
            user = self.d.get_user_id(user)
            user = user['user']
            try:
                results = self.d.get_reports(user)
                return self.generate_response(results,200,type="json")
            except:
                return self.generate_response(self.error,500)
        

        @app.route('/reports',methods=['GET'])
        @self.verify_token
        def reports(user):
            try:
                results = self.d.get_reports()
                return self.generate_response(results,200,type="json")
            except:
                return self.generate_response(self.error,500)


    def generate_response(self,message,code=200,type="text"):
        response = None
        if type == "json":
            response = self.app.response_class(
                response=json.dumps(message),
                status=code,
                mimetype='application/json'
            )
        else:
            response = self.app.response_class(
                response=message,
                status=code,
                mimetype='text/plain'
            )
        return response


    def verify_token(self,fun):
        @wraps(fun)
        def verifing(*args,**kwargs):
            auth_headers = request.headers.get('Authorization', '').split()
            token = auth_headers[1]
            result = False
            try:
                result = self.tg.get_desc_token(token)
                if result != False:
                    user_id = str(list(result.keys())[0])
                    self.token = True
                    return fun(user_id)
                else:
                    resp = "Token Incorrecto"
                    return self.generate_response(resp,302)
            except Exception as e:
                resp = "Error en el servidor"
                return self.generate_response(resp,500)
        return verifing


    def verify_token_p(self,fun):
        @wraps(fun)
        def verifing(*args,**kwargs):
            auth_headers = request.headers.get('Authorization', '').split()
            token = auth_headers[1]
            result = "False"
            try:
                result = self.tg.get_desc_token(token)
                user_id = str(list(result.keys())[0])
                self.token = True
                return fun(*args,**kwargs)
            except Exception as e:
                return str(e)
        return verifing
        