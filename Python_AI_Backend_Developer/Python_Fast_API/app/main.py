from fastapi import FastAPI
from app.routers.routers import api_router

app = FastAPI(title='Fast API DIO')
app.include_router(api_router)
