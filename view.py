from datetime import *
from tabnanny import check
from main import app
from models import Todo,LOGIN
from fastapi import Depends, HTTPException
from passlib.hash import sha256_crypt
from controls import Handle
import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

def create_access_token(data: dict):
    file_copy = data.copy()
    expire = datetime.now() + timedelta(minutes=25)
    file_copy.update({'expire': expire.minute})
    encode_jwt = jwt.encode(playload = to_copy, key='OkeToken124342@', algorithm='HS256')
    return encode_jwt

def verify_token(token: str, credential_exception):
    try:
        payload = jwt.decode(playload=token, key='OkeToken124342@', algorithm='HS256')
        username: str = payload.get("sub")
        if username is None:
            raise credential_execption
    except Exception:
    raise credential_execption
    
oauth = OAuth2PasswordBearer(tokenUrl='local')
    
def get_current_user(token: str = Depends(oauth)):
credentials_exception = HTTPException(
    status_code=401,
    detail="System couldn't validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
return verify_token(token, credentials_exception)



@app.post("/reg")
async def epep(usr:Todo=Depends()):
    db=Handle()
    hashing=sha256_crypt.hash(usr.password)
    if db.check(usr.email) is not None:
        raise HTTPException(status_code =400,detail="email sudah digunakan")
    data=(usr.username,usr.email,hashing,usr.position_job)
    db.reg(data)
    return {"message":"oke","status":200}

@app.post("/login")
async def local(usr:LOGIN=Depends()):
    db=Handle()
    check=db.login(usr.username)
    access_token = create_access_token(data={'sub': check['username']})
    if check is None:
        raise HTTPException(status_code=400,detail="username belum terdaftar")
    if sha256_crypt.verify(usr.password,check["password"]):
        return {"message":"selamat anda berhasil","status":200, 'auth': access_token}
    else:
        raise HTTPException(status_code=400,detail="password salah")










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
