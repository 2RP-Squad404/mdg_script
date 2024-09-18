import uvicorn
from fastapi import FastAPI
from routes import router

app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
