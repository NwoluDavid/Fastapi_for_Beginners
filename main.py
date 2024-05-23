from fastapi import FastAPI
from fastapi.responses import Response

app= FastAPI()

@app.get("/")
# getting started with our app.
async def root():
    welcome={"welcome:home"}
    return welcome

@app.post("/" ,
status_code=201,
description="this is the post route"
)
async def post():
    # """this is the post route
    # """
    return {"message":"success"}

@app.put("/" , status_code=201 , description= "This is our put routes", deprecated=True )
# You can choose to deprecate a route
# by using the deprecated varible and setting to true.
async def hello():
    return {"message":"hello world"}


