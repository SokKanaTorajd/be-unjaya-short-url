from datetime import *
from main import app
from models import Todo
from fastapi import Depends, HTTPException
from passlib.hash import sha256_crypt
from controls import Handle

@app.post("/reg")
async def epep(usr:Todo=Depends()):
    db=Handle()
    hashing=sha256_crypt.hash(usr.password)
    if db.check(usr.email) is not None:
        raise HTTPException(status_code =400,detail="email sudah digunakan")
    data=(usr.username,usr.email,hashing,usr.position_job)
    db.reg(data)
    return {"message":"oke","status":200}
# @app.get("/")
# async def test():
#     return {"nama":"moudy"}

# data =[]
# @app.post("/post")

# async def post(todo:Todo=Depends()):
#     new= {
#         "nama":todo.nama,
#         "username":todo.username,
#         "password":sha256_crypt.hash(todo.password),
#         "email":todo.email
#     }
#     data.append(new)
#     return data
    
# @app.get("/put/{id}")
# async def put_data(id:int):
#     try:
#         return data[id]
#     except:
#         raise HTTPException(status_code=404, detail="Todo Not Found")

# @app.put("/get/{id}")
# async def update_todo(id:int, todo:Todo):
#     try:
#         data[id] = todo
#         return data[id]
#     except:
#         raise HTTPException(status_code=404, detail="Todo Not Found")

# @app.delete("/delete/{id}")
# async def deleta_data(id:int):
#     try:
#         obj = data[id]
#         data.pop(id)
#         return obj
#     except:
#         raise HTTPException(status_code=404, detail="Todo Not Found")

# @app.get("/get")
# async def getall():
#     return data
