from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from app.routes import router

app = FastAPI()

app.include_router(router)

register_tortoise(
    app,
    db_url='postgres://username:password@postgres:5432/database_name',
    modules={'models': ['app.models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
