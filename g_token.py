import jwt
from dotenv import load_dotenv
import os
class TokenGen:
    load_dotenv()
    def __init__(self,message):        
        self.secret = os.getenv('SECRET_SESSION')
        token_bytes = jwt.encode(message, self.secret, algorithm='HS256')
        self.token = token_bytes
        print(self.token)

    @property
    def get_token(self):
        return self.token
    
    def get_desc_token(self):
        token_decode = jwt.decode(self.token,self.secret,algorithm='HS256')
        return token_decode