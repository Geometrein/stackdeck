import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers.endpoints import endpoints
from routers.views import views

app = FastAPI()
app.include_router(endpoints)
app.include_router(views)
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
