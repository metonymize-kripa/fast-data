from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

data_dictionary={}
dictionary_initialized=False

class Query(BaseModel):
    data_key: str = None
    max_rows: int = 10

class Data(BaseModel):
    data_key: str = None
    data_value: float = None

@app.post("/query/", response_model=Data)
async def query(query: Query):
    global dictionary_initialized
    if not dictionary_initialized:
        raise HTTPException(status_code=404, detail="Dictionary not initialized")
    if query.data_key in data_dictionary:
        return {
            "data_key": query.data_key,
            "data_value": data_dictionary[query.data_key]
        }
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/initialize")
def initialize():
    global dictionary_initialized
    global data_dictionary
    try:
        with open('sp500_sga_2021.tsv') as fr:
            for line in fr:
                [data_key,data_value]=line.strip().split('\t')
                data_dictionary[data_key]=float(data_value)
        dictionary_initialized=True
        return {
        "message": "File loaded"
        }
    except:
        dictionary_initialized=False
        return {
            "message": "Initialization failed"
        }

@app.get("/")
async def read_root():
    return {"Hello": "World"}
