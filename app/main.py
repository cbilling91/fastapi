from fastapi import FastAPI

app = FastAPI(
    title="Hi 👋"
)

@app.get("/")
async def hello():
    return {"Hello": "World 👋"}