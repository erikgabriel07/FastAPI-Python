from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schema import Base

app = FastAPI(title="CRUD - FastAPI Example",
              docs_url="/docs", redoc_url="/redocs")


engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
