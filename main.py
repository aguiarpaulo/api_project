from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hi": "The Test is Perfect!"}

products = [{
    "id":1,
    "name": "Iphone16",
    "description": "cellphone",
    "value": 5000
},
{
    "id":2,
    "name": "keyboard",
    "description": "device",
    "value": 50
},
{
    "id":3,
    "name": "mouse",
    "description": "device",
    "value": 50
}]

@app.get("/products")
def product_list_return():
    return products

@app.get("/") #request
def ola_mundo(): #response
    return {"ola": "Mundo"}