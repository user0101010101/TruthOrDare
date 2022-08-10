from fastapi import FastAPI, Query, Path, Body
import uvicorn
from typing import List
from schemas import Book, Autor, BookOut, RandQuestionOut
app = FastAPI()
from db.mongo import OneQuestion
import  socket

# sock = socket.socket()
# sock.bind(('', 8000))
# sock.listen(1)
# conn, addr = sock.accept()
# print(addr)
@app.get("/")
async def home():
    return {"Hello user"}
# @app.get("/{pk}")
# def get_item(pk: int, q: str = None):
#     return {"key": pk, "q": q}
#
# @app.get("/user/{pk}/items/{item}")
# def get_user_item(pk: int,item: str):
#     return {"user": pk, "item": item}
# @app.post("/book", response_model_exclude_unset=True, response_model_exclude={"item"})# не показывать пустые данные
# def create_book(item: Book, autor: Autor, quantity: int = Body(...)):
#     return {"item": item, "autor": autor, "quantity": quantity}

@app.get('/get_new_question', response_model=RandQuestionOut)
async def get_new_question():
    return await OneQuestion()

if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='192.168.50.191',
        port=8000,
        reload=True
    )


# @app.post("/book", response_model=BookOut)
# def create_book(item: Book):
#     return BookOut(id=3, **item.dict())
# @app.post("/autor")
# def create_autor(autor: Autor = Body(..., embed=True)):
#     return {"autor": autor}
#
# #Query - validation
# @app.get("/book")
# def get_book(q: List[str] = Query(["test", "test2"], min_length=2, description="Search book")): #... - обязательный параметр или "Test" - дефолтное значение
#     return q
# @app.get("/book/{pk}")
# def get_single_book(pk: int = Path(..., gt=1, lt=10)):
#     return {"pk": pk}