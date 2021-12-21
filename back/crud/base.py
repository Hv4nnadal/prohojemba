from databases import Database


class BaseCRUD:
    def __init__(self, database: Database) -> None:
        self.database = database