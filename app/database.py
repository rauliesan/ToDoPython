# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@db.ixmujviepzpsxkycnfhv.supabase.co:5432/postgres" # para local pero da problemas en render porque no funciona con ipv4
SQLALCHEMY_DATABASE_URL = "postgresql://postgres.ixmujviepzpsxkycnfhv:password@aws-0-eu-north-1.pooler.supabase.com:6543/postgres" # fuciona con ipv4

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()