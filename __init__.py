from logging import exception
from flask import Flask, request
import json
from data import Data
from data_aux import DataAux
from g_token import TokenGen
from functools import wraps
import os

token = False
tg = TokenGen()
d = Data()
da = DataAux()
error = "No se pudo resolver la solicitud"

app = Flask(__name__)

_port = os.environ.get('PORT', 5000)


def generate_response(message,code=200,type="text"):
    response = None
    if type == "json":
        response = app.response_class(
            response=json.dumps(message),
            status=code,
            mimetype='application/json'
        )
    else:
        response = app.response_class(
            response=message,
            status=code,
            mimetype='text/plain'
        )
    return response


def verify_token(fun):
    @wraps(fun)
    def verifing(*args,**kwargs):
        auth_headers = request.headers.get('Authorization', '').split()
        token = auth_headers[1]
        result = False
        try:
            result = tg.get_desc_token(token)
            if result != False:
                user_id = str(list(result.keys())[0])
                token = True
                return fun(user_id)
            else:
                resp = "Token Incorrecto"
                return generate_response(resp,302)
        except Exception as e:
            resp = "Error en el servidor"
            return generate_response(resp,500)
    return verifing


def verify_token_p(fun):
    @wraps(fun)
    def verifing(*args,**kwargs):
        auth_headers = request.headers.get('Authorization', '').split()
        token = auth_headers[1]
        result = "False"
        try:
            result = tg.get_desc_token(token)
            user_id = str(list(result.keys())[0])
            token = True
            return fun(*args,**kwargs)
        except Exception as e:
            return str(e)
    return verifing

@app.route('/')
def index():
    return "Projectify"

@app.route('/login',methods=['POST'])
def login():
    tg.change_secret()
    request_data = request.args.to_dict()
    list_params = {"user":"text","pass":"text"}
    res,errors = da.validate_params(request_data,list_params)
    if len(errors) > 0:
        return generate_response(errors,200)
    user = res['user']
    passd = res['pass']
    print("333")
    res = d.get_user(user,passd)
    print(res)
    if res != None:
        try:
            message = {res[1]:res[0]['user']}
            token = tg.gen_token(message)
            result = tg.get_token()
            return generate_response(result,200)
        except:
            return generate_response(error,500)
    else:
        return generate_response("Usuario o contraseña incorrectos",200)


@app.route('/new_user',methods=['POST'])
def new_user():
    request_data = request.args.to_dict()
    list_params = {"user":"text","pass":"text"}
    request_data,errors = da.validate_params(request_data,list_params)
    if len(errors) > 0:
        return generate_response(errors,200)
    try:
        print("22")
        user = request_data['user']
        passd = request_data['pass']
        resp = d.new_user(user,passd)
        print(resp)
        return generate_response(resp,200)
    except:
        return generate_response(error,500)


@app.route('/verify',methods=['POST'])
@verify_token
def verify(user):
    print(user)
    user = d.get_user_id(user)
    print(user)
    return generate_response("Yes",200)


@app.route('/new_project',methods=['POST'])
@verify_token
def new_project(user):
    request_data = request.args.to_dict()
    list_params = {"start":"date","end":"date","name":"text"}
    request_data,errors = da.validate_params(request_data,list_params)
    if len(errors) > 0:
        return generate_response(errors,200)
    try:
        start = request_data["start"]
        end = request_data["end"]
        name = request_data["name"]
        print(f'Name {name} - Start {start} - End {end}')
        response = d.new_project(start,end,name)
        return generate_response(response,200)
    except:
        return generate_response(error,500)


@app.route('/new_report',methods=['POST'])
@verify_token
def new_report(user):
    request_data = request.args.to_dict()
    list_params = {"porcent":"number","week":"week","name":"text"}
    request_data,errors = da.validate_params(request_data,list_params)
    if len(errors) > 0:
        return generate_response(errors,200)
    try:
        porcent = request_data["porcent"]
        week = request_data["week"]
        name = request_data["name"]
        response = d.new_report(user,str(name),str(week),str(porcent))
        return generate_response(response,200)
    except:
        return generate_response(error,500)


@app.route('/reports/<user_name>',methods=['GET'])
@verify_token_p
def reports_name(user_name):
    list_params = {"user_name":"text"}
    request_data = {"user_name":user_name}
    request_data,errors = da.validate_params(request_data,list_params)
    if len(errors) > 0:
        return generate_response(errors,200)
    try:
        results = d.get_reports(user_name)
        return generate_response(results,200,type="json")
    except:
        return generate_response(error,500)


@app.route('/my_reports/',methods=['GET'])
@verify_token
def my_reports(user):
    user = d.get_user_id(user)
    user = user['user']
    try:
        results = d.get_reports(user)
        return generate_response(results,200,type="json")
    except:
        return generate_response(error,500)


@app.route('/reports',methods=['GET'])
@verify_token
def reports(user):
    try:
        results = d.get_reports()
        return generate_response(results,200,type="json")
    except:
        return generate_response(error,500)






if __name__ == '__main__':
    app.run(host='0.0.0.0', port=_port)
    