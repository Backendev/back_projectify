import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
from g_token import TokenGen
import os
from singleton import Singleton

class Data(metaclass=Singleton):
    def __init__(self):
        self.cred = credentials.Certificate(os.getenv('CONFIG_FIREBASE'))
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        self.user_col = self.db.collection(u'users')
        self.projects_col = self.db.collection(u'projects')
        self.reports_col = self.db.collection(u'reports')
    
    def get_user(self,user,passd=None,idu=None):
        docs = []
        if idu != None:
            users = list(self.user_col.where(u'user', u'==',user).stream())
            if users[0].id == idu:
                docs = users
        elif passd != None:
            docs = list(self.user_col.where(u'user', u'==',user).where(u'pass',u'==',passd).stream())
        else:
            docs = list(self.user_col.where(u'user', u'==',user).stream())
        l = len(list(docs))
        result = None
        if l > 0:
            for doc in docs:
                result = doc.to_dict(),doc.id
        return result
    def new_user(self,user,passd):
        user_old = self.get_user(user=user)
        result = None
        if user_old != None:
            result = False
        else:
            docs = list(self.user_col.stream())
            ids = int(len(docs))
            new_id = ids +1
            new_user = self.user_col.document(u''+str(new_id))
            new_user.set({
                u'user': user,
                u'pass':passd
            })
            result = True
        return result

