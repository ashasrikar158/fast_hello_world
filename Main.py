import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get('/')
def index():
    return {'Message': 'Welcome everyone!'}

