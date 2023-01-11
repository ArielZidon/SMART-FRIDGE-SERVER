import json
import firebase_admin
from fastapi import FastAPI
from typing import Optional
from firebase_admin import credentials, firestore

# os.environ["FIREBASE_AUTH_EMULATOR_HOST"] =  "127.0.0.1:9099"
# os.environ["FIRESTORE_EMULATOR_HOST"] = "127.0.0.1:8080"
from item import Item

app = FastAPI()
cred = credentials.Certificate('smart-fridge-c19d3-firebase-adminsdk-k1q6g-4051baf032.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://smart-fridge-c19d3-default-rtdb.firebaseio.com'
})

db = firestore.client()

users_ref = db.collection('costumer_accounts')
docs = users_ref.stream()
output = {}
for doc in docs:
    output[doc.id] = doc.to_dict()
    # print(doc.to_dict())
    # print(f'{doc.id} => {doc.to_dict()}')


# print(output['afik@gmail.com'])
# print(output['afik@gmail.com'])

# @app.get("/user/{user_id}")
# async def read_item(user_id: str):
#     item_ref = db.collection("costumer_accounts").document(user_id)
#     item_doc = item_ref.get()
#     if item_doc.exists:
#         item = item_doc.to_dict()
#         return json.dumps(item)
#     else:
#         return {"error": "item not found"}


def eq(passwors, key):
    return passwors == key


# def insert_new_account():
#     doc_ref = db.collection('costumer_accounts').document('arielTest')
#     doc_ref.set({
#         'name': 'ofir@gmail.com',
#         'password': '1234567',
#         'user_type': 'costumer'
#     })


@app.get("/users/{user_id}/{password}")
def read_user(user_id: str, password: str):
    user_ref = db.collection("costumer_accounts").document(user_id)
    user_doc = user_ref.get()
    if user_doc.exists:
        user_data = user_doc.to_dict()
        if eq(password, user_data['password']):
            return {user_id : "0"}
        else:
            return {"wrong password": "1"}
    else:
        return {"error": "2"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# if __name__ == '__main__':
#     insert_new_account()
