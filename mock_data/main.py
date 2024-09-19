import uvicorn
from fastapi import FastAPI
from config import settings
from routes import router

app = FastAPI(title=settings.API_TITLE, description=settings.API_DESCRIPTION, version=settings.API_VERSION)
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run(app, host=settings.API_HOST, port=settings.API_PORT)
