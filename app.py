from fastapi import FastAPI, Query


app = FastAPI(
    title="Test OpenAPI Spec",
    version="0.1.0",
    description="OpenAPI Specification",
)

"""
@app.get("/")
async def home(id: int = Query(..., gt=0)):
    return {"msg": f"Welcome {id}!"}
"""


@app.get("/no-bug")
async def home(id: int = Query(...)):
    return {"msg": f"Welcome {id}!"}
