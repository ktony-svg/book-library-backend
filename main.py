from fastapi import FastAPI
from database import engine
import models
from routes import books # <--- CORRECTED LINE HERE

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Ensure this line correctly uses books.router
app.include_router(books.router, prefix="/books", tags=["Books"])

@app.get("/")
def root():
    return {"message": "Welcome to the Book Library API"}
