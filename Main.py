from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from Routes.UserRoutes import router as user_router

app = FastAPI(
    title="CUSTOMS INTERCHANGE SERVICE",
    description="Web service for custom interchange system",
    version="1.0.0"
)

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # List of allowed origins
    allow_credentials=True,  # Allow cookies to be sent with requests
    allow_methods=["*"],     # HTTP methods to allow (GET, POST, etc.)
    allow_headers=["*"],     # HTTP headers to allow
)

app.include_router(user_router)