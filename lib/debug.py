#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_sandbox import Base, Student

engine = create_engine('sqlite:///students.db')

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

