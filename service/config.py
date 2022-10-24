"""
Global Configuration for Application
"""
import os


# Get configuration from environment
DATABASE_URI = os.getenv("DATABASE_URI")

# Build DATABASE_URI from environment if not found
if not DATABASE_URI:
    DATABASE_USER = os.getenv("DATABASE_USER", "postgres")
    DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "postgres")
    DATABASE_NAME = os.getenv("DATABASE_NAME", "postgres")
    DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
    DATABASE_URI = f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:5432/{DATABASE_NAME}"

# Configure SQLAlchemy
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret for session management
SECRET_KEY = os.getenv("SECRET_KEY", "s3cr3t-key-shhhh")
