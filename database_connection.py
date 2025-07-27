from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = 'sqlite:///.currencies.db'   # Connecting to SQLite databse

engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})    # Creating engine

session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()