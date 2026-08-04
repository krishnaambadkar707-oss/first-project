from Database.database import Base
from Database.database import engine

import Database.models

Base.metadata.create_all(bind=engine)

print("Database Created Successfully.")