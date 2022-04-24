from typing import Optional
from fastapi import FastAPI, responses
from fastapi.responses import HTMLResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel, Field
from bson import ObjectId
import os

app = FastAPI()


class Connection(object):
    client = None

    @classmethod
    def singleton(
        cls, host:str = 'localhost', port:int=27017, 
        username:str = 'root', password:str = '', 
        name:str='Website'
    ):
        client = AsyncIOMotorClient(
            'mongodb://{}:{}'.format(host, port),
            username=username,
            password=password,
        )

        cls.client = client[name]
        return cls.client

Connection.singleton(
    host=os.getenv('MONGO_INITDB_HOST'),
    username=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
    password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
    name=os.getenv('MONGO_INITDB_DATABASE'),
)

    
class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class User(BaseModel):
    id: Optional[PyObjectId] = Field(alias='_id')
    name: str
    email:str
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }


@app.get("/", response_class=HTMLResponse)
async def index(title: Optional[str] = 'default'):
    html_content = f"""
    <html>
        <head>
            <title>{title}</title>
        </head>
        <body>
            <h1>{title}!</h1>
            <p>TEMPLATE</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/user")
async def list():
    user_collection = Connection.client.get_collection("users")
    users = []
    async for user in user_collection.find():
        users.append(User(**user))
    return users


@app.get("/user/{id:str}")
async def details(id:str):
    user = await Connection.client["users"].find_one({"_id":ObjectId(id)});
    return User(**user) if user else None


@app.post("/user/create")
async def create(user:User):
    Connection.client["users"].insert_one({
        "name":user.name, 
        "email": user.email,
    })
    return responses.RedirectResponse("/user", 302)
    

@app.put("/user/{id:str}")
async def update(id:str, user:User):
    Connection.client["users"].update_one(
        {'_id': ObjectId(user.id)},
        { '$set':{"name":user.name, "email": user.email}}
    )
    return responses.RedirectResponse("/user", 302)
    

@app.delete("/user/{id:str}")
async def delete(id:str):
    Connection.client["users"].delete_one({"_id":ObjectId(id)})
    return responses.RedirectResponse("/user", 302)
