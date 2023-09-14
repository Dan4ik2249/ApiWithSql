#!/usr/bin/python3
from typing import Union
from fastapi import FastAPI
import uvicorn
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
async def start():
    """Начальная страница"""
    return {"massage": "Hello"}

@app.get("/products")
async def read_root():
    con = sqlite3.connect("market.db")
    cur = con.cursor()
    res = cur.execute("SELECT DISTINCT name FROM products")
    top = res.fetchall()

    con.close()
    print(top)
    return top #{"Список телефонов": top}#

@app.get("/product/{id}")
async def read_root(id :int):
    return {"id": id}

@app.get("/products/{name}")
async def func_name(name):
    name_phone = (name,)
    con = sqlite3.connect("market.db")
    cur = con.cursor()
    res = cur.execute("SELECT name, model FROM products where name=?", name_phone)
    model = res.fetchall()
    print(model)
    con.close()
    return model #{"Список доступных моделей": model}#

@app.get("/products/names/{id}")
async def func_name(id :int):
    return {"id": id}

@app.get("/products/{name}/{model}")
async def show_color(model, name):
    model_phone = (model, name)
    con = sqlite3.connect("market.db")
    cur = con.cursor()
    res = cur.execute("SELECT p.name, p.model, clr.color, pl.price FROM products p, clr, pl where p.id=clr.id and p.id=pl.id and model=? and name=?",  model_phone)
    color = res.fetchall()
    
    print(color)
    con.close()
    return color #{"Список доступных цветов": color}#

@app.get("/products/names/models/{id}")
async def show_color(id :int):
    return {"id": id}

if __name__ == "__main__":
    uvicorn.run(app) 
