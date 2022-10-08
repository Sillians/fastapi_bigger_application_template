from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header
from .internal.admin import router as admin_router
from .routers.items import router as items_router
from .routers.users import router as users_router

app = FastAPI(dependencies=[Depends(get_query_token)])


app.include_router(users_router)
app.include_router(items_router)
app.include_router(
    admin_router,
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={418: {"description": "I'm a teapot"}},
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
