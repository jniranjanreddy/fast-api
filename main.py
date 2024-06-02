from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    return {"Hello": {"Name": "Niranjan"}}


@app.get("/blog/?limit=10&published=true")
def show(id: str):
    return {"data": id}

@app.get("/blog/unpublished")
def show():
    return {"data": "All Unpublished"}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {"1","2"}}