from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/", response_model=Item)
async def create_item(item: Item):
    return item

@app.get("/")
async def read_root():
    return {"Hello": "World"}
