from typing import Union

from fastapi import FastAPI

from precent import Precent

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/precent")
def precent():
    return Precent.result_prcent('mushroom.csv', 'class')

