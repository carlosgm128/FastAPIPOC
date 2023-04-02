from fastapi import FastAPI
from subapps.appv1 import appv1 as v1
from subapps.appv2 import appv2 as v2
from routes.users_router import user_router
from routes.item_router import item_router

app = FastAPI()
app.mount("/app/v1", v1)
app.mount("/app/v2", v2)
app.include_router(user_router, prefix='/users')
app.include_router(item_router, prefix='/items')
