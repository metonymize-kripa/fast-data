from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

wise_dictionary={"Back Office":2.0}
    
def wise_parser(symbol):
  if 
    initialize()
    try:	
        return wise_dictionary[symbol]	
    except:	
        return -1

skills_dictionary={"WISE":wise_parser}	

def dispatch_skill_parser(skill, symbol):
    try:	
        return skills_dictionary[skill](symbol)	
    except:	
        return 0
    
@app.get("/parse/{parameter}")
def parse(parameter: str):
    parsed_parameter_list = parameter.strip().split('%20')
    num_parameters_parsed = len(parsed_parameter_list)
    
    #return {"Output":parsed_parameter_list}

    if  num_parameters_parsed == 2:	
        parsed_symbol = parsed_parameter_list[0].upper()	
        parsed_skill = parsed_parameter_list[1].upper()	
        skill_returned_value = dispatch_skill_parser(parsed_skill, parsed_symbol)	
    else:	
        return {"symbol": "no symbol",	
                "skill": "no skill",	
                "skill_output": "no output",	
                "datetime": "no time"}	
    try:	
        return {"symbol": parsed_symbol,	
                "skill": parsed_skill,	
                "skill_output": skill_returned_value,	
                "datetime": datetime.date.today()}#datetime.now().time()}	
    except:	
        return {"symbol": "no symbol",	
                "skill": "no skill",	
                "skill_output": "no output",	
                "datetime": "no time"}	           
    
@app.get("/initialize")
def initialize():
    try:
        with open('wise.tsv') as fr:
            for line in fr:
                [symbol,mention]=line.strip().split('\t')
                wise_dictionary[symbol]=float(mention)
                wise_dictionary[symbol]=float(mention)
        return {
        "message": "Files initialized"
        }
    except:
        return {
            "message": "Initialization failed"
        }

@app.get("/")
def main():
    return {
        "message": "Hello, world!"
    }
