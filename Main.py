import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'Message': 'This is only a message!'}
