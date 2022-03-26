import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from g_token import TokenGen





message = {1:'123456'}
token = TokenGen(message)
print(token.get_token.decode())
print(f'Dec => {token.get_desc_token()}')


cred = credentials.Certificate("projectify10-firebase-adminsdk-ektvs-08d4e6b934.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'users')
docs = doc_ref.stream()
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')
print("22")
doc_ref = db.collection(u'users').document(u'1')
doc_ref.set({
    u'first': u'Ada',
    u'last': u'Lovelace',
    u'born': 1815
})

docs = list(db.collection(u'users').where(u'first', u'==',u'Ada').stream())
l = len(list(docs))
print(l)
res_dict = {}
# print(len(list(docs)))
if l > 0:
    print("mayor")
    for doc in docs:
        res_dict = doc.to_dict()
        print(f'{doc.id}22 => {doc.to_dict()}')
print("444")
if len(res_dict) > 0:
    print(f'Result {res_dict["last"]}')