from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()
instrumentator = Instrumentator().instrument(app)


# it will generate /metrics endpoint
@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}
