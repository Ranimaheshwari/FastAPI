from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def index():
    return {'data':{'name':"rani"}}

@app.get("/about")
async def about():
    return {'data': 'about page'}