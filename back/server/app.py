from fastapi import FastAPI, Request, Depends, Header

app = FastAPI()
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}