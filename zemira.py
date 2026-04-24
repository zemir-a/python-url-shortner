from fastapi import FastAPI

app = FastAPI(title="Zemira FastAPI App")

@app.get("/")
def home():
    return {"message": "FastAPI is running"}



u
