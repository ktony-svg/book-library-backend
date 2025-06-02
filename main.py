# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Import CORS middleware
from database import engine
import models
from routes import books

app = FastAPI()

# --- ADD CORS MIDDLEWARE FOR LOCAL DEVELOPMENT ---
# Allows your frontend (e.g., if running on http://127.0.0.1:5500 from Live Server)
# to make requests to your backend (http://127.0.0.1:8000).
origins = [
    "http://localhost",
    "http://localhost:8000", # Your backend itself
    "http://127.0.0.1",
    "http://127.0.0.1:8000", # Your backend itself
    "http://localhost:3000", # Common for React/Vue dev servers
    "http://localhost:5000", # Another common dev server port
    "http://127.0.0.1:5500", # Common for VS Code Live Server
    # Add any other local origins your frontend might run on
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"], # Allows all headers
)
# --- END CORS MIDDLEWARE ---

# This creates the database tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# Include your books router
app.include_router(books.router, prefix="/books", tags=["Books"])

@app.get("/")
def root():
    return {"message": "Welcome to the Book Library API"}
