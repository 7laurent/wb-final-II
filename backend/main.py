from fastapi import FastAPI
import sqlite3
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def home():
    return {"message": "Backend working"}

@app.get("/users")
def users():
    return {"users": ["Ella", "Laurent"]}

@app.get("/products")
def products():
    return {"products": ["Phone", "Laptop"]}
@app.get("/unemployment")
def unemployment():

    conn = sqlite3.connect("data/unemployment.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM unemployment LIMIT 10")

    data = cursor.fetchall()

    conn.close()

    return {"data": data}