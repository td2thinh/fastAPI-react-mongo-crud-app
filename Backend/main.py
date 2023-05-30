from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from decouple import config

# ENV Variables
PORT = config('PORT')

# APP Object
app = FastAPI()

origins = ['https://localhost:' + str(PORT)]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=['*']
)

print("Starting server on port " + str(PORT))


@app.get('/')
def index():
    return {'message': 'Hello World'}
