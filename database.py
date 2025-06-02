# database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./books.db"

# Create the SQLAlchemy engine
# connect_args={"check_same_thread": False} is needed for SQLite to allow multiple threads
# to interact with the database, which is common in web applications.
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Configure a SessionLocal class to create database sessions
# autocommit=False: Transactions are not committed automatically
# autoflush=False: Changes are not flushed to the database until commit
# bind=engine: Binds the session to our SQLAlchemy engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependency to get a database session
# This function will be used with FastAPI's Depends()
def get_db():
    """
    Provides a SQLAlchemy database session to FastAPI route functions.
    The session is automatically closed after the request is processed.
    """
    db = SessionLocal() # Create a new session
    try:
        yield db # Yield the session to the calling function (the route)
    finally:
        db.close() # Ensure the session is closed after the request
