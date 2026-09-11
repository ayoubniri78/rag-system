from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions import AppException
from routes import router

app = FastAPI()
app.include_router(router,prefix="/api/v1")

@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,
    exc: AppException
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": exc.code,
            "message": exc.message
        }
    )
