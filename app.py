from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

data_dictionary={}

class Item(BaseModel):
    name: file_name
    description: str = None
    company: str
    sga: float = None

@app.post("/query", response_model=Item)
async def create_item(item: Item):
    return item

@app.get("/initialize")
def initialize():
    try:
        with open('sp500_sga_2021.tsv') as fr:
            for line in fr:
                [data_key,data_value]=line.strip().split('\t')
                data_dictionary[data_key]=float(data_value)
        return {
        "message": "File loaded"
        }
    except:
        return {
            "message": "Initialization failed"
        }

@app.get("/")
async def read_root():
    return {"Hello": "World"}
