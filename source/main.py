from src.config import app
from src.routes import api_router
from uvicorn import run

app.include_router(api_router)


@app.get("/")
def home():
    return {"message": "Welcome to my application!"}


if __name__ == "__main__":
    run("main:app", reload=True)
