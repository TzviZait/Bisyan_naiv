from typing import Union

from fastapi import FastAPI

from geting_data import Geting_Data
from precent import Precent

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/precent")
def precent():
    return Precent.result_prcent(Geting_Data.get_data("buy_computer_data.csv"), 'Buy_Computer')

