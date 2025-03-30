from fastapi import FastAPI
from core.db import init_db
from api.user_api import router


app = FastAPI(
    title='Bookly',
    description='A RESTful API for a book review web service',
    version='v1',
)

@app.on_event("startup")
async def on_startup():
    await init_db()


app.include_router(router,prefix=f"/api/users",tags=["users"])
