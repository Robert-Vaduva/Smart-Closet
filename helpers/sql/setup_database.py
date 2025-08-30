from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# Define base class
Base = declarative_base()
DEBUG = False


# Create database connection
engine = create_engine("sqlite:///data/smart-closet.db", echo=DEBUG)
Session = sessionmaker(bind=engine)
session = Session()
