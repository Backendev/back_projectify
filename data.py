import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from dotenv import load_dotenv
from g_token import TokenGen
import os
from singleton import Singleton
from data_aux import DataAux
from datetime import datetime

class Data(metaclass=Singleton):
    def __init__(self):
        self.cred = credentials.Certificate(os.getenv('CONFIG_FIREBASE'))
        firebase_admin.initialize_app(self.cred)
        self.db = firestore.client()
        self.user_col = self.db.collection(u'users')
        self.projects_col = self.db.collection(u'projects')
        self.reports_col = self.db.collection(u'reports')
        self.da = DataAux()
    def get_project(self,name):
        project = list(self.projects_col.where(u'name', u'==',name).stream())
        l = len(list(project))
        result = None
        if l > 0:
            for doc in project:
                result = doc.to_dict(),doc.id
        return result
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
    def split_date(self,date):
        sp_date = date.split("-")
        return int(sp_date[0]),int(sp_date[1]),int(sp_date[2])

    def new_project(self,start,end,name):
        start_year,start_month,start_day = self.split_date(start)
        end_year,end_month,end_day = self.split_date(end)
        start_date  = datetime(start_year,start_month,start_day)
        end_date  = datetime(end_year,end_month,end_day)
        list_weeks = self.da.weeks_range(start_date,end_date)
        project_old = self.get_project(name)
        if project_old != None:
            result = False
        else:
            projects = list(self.projects_col.stream())
            ids = int(len(projects))
            new_id = ids +1
            new_project = self.projects_col.document(u''+str(new_id))
            new_project.set({
                u'name':name,
                u'start_date':str(start_date),
                u'end_date':str(end_date),
                u'weeks_list':list_weeks
            })
            result = True
        return result
    def new_report(self,user,name,week,porcent):
        project_old = self.get_project(name)
        print(project_old)
        result = None
        if project_old == None:
            result = False
        else:
            project_id = project_old[1]
            project = project_old[0]
            print(f'project: {project} - {str(type(project))}')
            print(f'project_id: {project_id} - {str(type(project_id))}')
            weeks = list(project['weeks_list'])
            print(weeks[0])
            if week in weeks:
                print("yes")
                reports = list(self.reports_col.stream())
                ids = int(len(reports))
                new_id = ids +1
                new_report = self.reports_col.document(u''+str(new_id))
                new_report.set({
                    u'user':user,
                    u'project':str(project_id),
                    u'week':str(week),
                    u'porcent':porcent
                })
                result = True
            else:
                print("no")





