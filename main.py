from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()

@app.get("/")
def index():
    return {"Hello": {"Name": "Niranjan"}}

@app.get("/blog")
def index(limit, published: bool = True, sort: Optional[str] = None):
    # return published
    if published:
        return {"data": f"{limit} Published Blogs"}
    else:
        a = "Rama"
        return {"10 Bolgs from the database", a}






# @app.get("/blog/?limit=10&published=true")
# def show(id: str):
#     return {"data": id}

# @app.get("/blog/unpublished")
# def show():
#     return {"data": "All Unpublished"}
class Blog(BaseModel):
    title: str
    body: str
    published: bool


@app.get("/blog/{id}/comments")
def comments(id, limit=10):
    return {"data": {"1","2","4","3", id}}
    


@app.post("/blog")
def create_blog(request: Blog):
    return request
    return {"Blog is created"}



