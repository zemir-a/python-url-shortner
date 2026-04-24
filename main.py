from fastapi import FastAPI

app = FastAPI(title="Zemira FastAPI App")

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

@app.get("/index")
async def index():
    return {"message": "Hello, world!"}

@app.get("/zamira")
async def zamira():
    return {"message": "Hello, Zamira!"}