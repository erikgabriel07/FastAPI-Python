from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .schema import Base

app = FastAPI(title="CRUD - FastAPI Example",
              docs_url="/docs", redoc_url="/redocs")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)
