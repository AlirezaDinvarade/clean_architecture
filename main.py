from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from presentation.routes import auth, users


app = FastAPI()

# Allowed frontend origins
origins = [
    "http://localhost:3000",
    "http://localhost:3001",
    "http://localhost:3002",
]

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

