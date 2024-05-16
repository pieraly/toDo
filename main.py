
from fastapi import FastAPI , HTTPException

import routers.router_auth

import routers.router_todo

from documentation.description import api_description

app  = FastAPI(
    title = "Todo List",
    description=api_description,

)


app.include_router(routers.router_auth.router)
app.include_router(routers.router_todo.router)