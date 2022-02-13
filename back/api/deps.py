from typing import Generator

from back.common.db import Session

def get_db_connection() -> Generator:
    db = Session()
    try:
        yield db
    finally:
        db.close()
