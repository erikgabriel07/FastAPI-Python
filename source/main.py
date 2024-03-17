from src.config import app
from src.routes import api_router

from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from uvicorn import run


app.include_router(api_router)


@app.get("/")
def home():
    return {"message": "Welcome to my application!"}


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder(
            {"detail": exc.errors(), "message": "Invalid name field!"})
    )


if __name__ == "__main__":
    run("main:app", reload=True)
