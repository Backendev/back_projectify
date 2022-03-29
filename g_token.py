import jwt
from dotenv import load_dotenv
import os,random
from singleton import Singleton


class TokenGen(metaclass=Singleton):
    
    load_dotenv()
    
    
    def __init__(self):
        self.secret = ["eftdrnkbi","eyhfgijfui"]
        self.token = None
    

    def gen_token(self,message):
        self.token = jwt.encode(message, random.choice(self.secret), algorithm='HS256')


    def get_token(self):
        return self.token


    def get_desc_token(self,token):
        token_decode = None
        for i in self.secret:
            try:
                token_decode = jwt.decode(token,i,algorithms=['HS256'])
            except:
                pass
            if token_decode != None:
                return token_decode        
        return False
    
    
    def change_secret(self):
        s = os.environ.get('SECRET_SESSION',os.getenv('SECRET_SESSION'))
        if len(self.secret) < 6:
            self.secret.append(''.join(random.sample(s,len(s))))
