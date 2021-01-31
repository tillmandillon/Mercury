from fastapi import FastAPI
from users import get_hash, verify_password
from fastapi.templating import Jinja2Templates
engine=None
import yaml
with open("secret.yaml","r") as file:
    config=yaml.safe_load(file)

def get_engine():
    global engine
    if engine is not None:
        return engine
    from sqlalchemy import create_engine
    username=config["username"]
    password=config["password"]
    engine = create_engine(f"postgresql://{username}:{password}@localhost/database")
    return engine
    
import sqlalchemy
app = FastAPI()
from sqlalchemy import Table, MetaData, Column, Integer, String
metadata=MetaData(get_engine())

users=Table("users",
            metadata,
            Column("user_id",Integer,primary_key=True),
            Column("username",String,nullable=False),
            Column("password_hash",String,nullable=False),
            Column("email",String,nullable=False))

metadata.create_all(bind=get_engine())

Mercury = Jinja2Templates(directory="frontend")

@app.get("/")
async def root():
    return Mercury.TemplateResponse("index.html", {"request": request})

@app.get("/users")
def get_users():
    query="SELECT * FROM users"
    usernames=[]
    with get_engine().connect() as connection:
        result=connection.execute(query)
        for row in result:
            usernames.append(row["username"])        
    return usernames

@app.post("/users")
def register_user(username: str, password: str):
    _hash=get_hash(password)
    params={"username":username,"password_hash":_hash}
    query=sqlalchemy.insert(users).values(**params)
    print(str(query))
    with get_engine().connect() as connection:
        result=connection.execute(query)

@app.on_event("startup")
async def startup():
    get_engine()