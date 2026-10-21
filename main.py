from fastapi import FastAPI

app = FastAPI(title="Mobin API")


@app.get("/")
def home():
    return {
        "message": "Welcome to Mobin API!",
        "status": "online"
    }


@app.get("/api/status")
def status():
    return {
        "owner": "Mobin",
        "status": "active",
        "version": "1.0"
    }
