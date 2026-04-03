from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def say_hello():
    return "Hello world from FastAPI"

@app.get("/hello/{name}")
def hello_name(name:str):
    return f"HEllo {name}"