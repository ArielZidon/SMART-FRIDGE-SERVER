import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials
from firebase_admin import db

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello":"world"}