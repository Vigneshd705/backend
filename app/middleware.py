from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

# Example of custom middleware
class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        # Add custom logic (e.g., logging, modifying response)
        return response

def custom_middleware_setup(app: FastAPI):
    app.add_middleware(CustomMiddleware)
