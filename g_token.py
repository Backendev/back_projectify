import jwt
from dotenv import load_dotenv
import os,random
from singleton import Singleton


class TokenGen(metaclass=Singleton):
    load_dotenv()
    def __init__(self):
        self.secret = None
        self.token = None
    
    def gen_token(self,message):
        self.token = jwt.encode(message, self.secret, algorithm='HS256')

    def get_token(self):
        return self.token
    
    def get_desc_token(self,token):
        token_decode = jwt.decode(token,self.secret,algorithms=['HS256'])
        return token_decode
    
    def change_secret(self):
        s = os.getenv('SECRET_SESSION')
        self.secret = ''.join(random.sample(s,len(s)))
