import uvicorn
from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from hoses.hoses import HoseFabric as fabric

app = FastAPI()

@app.get('/fiftyone_check')
def check_fiftyone():
    fifty_one_first = fabric.get_hose(51)
    return JSONResponse({
        "51 рукав тестовый":fifty_one_first.__dict__()
    })

if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host='127.0.0.1', 
        port=8080
    )

