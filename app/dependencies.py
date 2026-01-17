from app.database import DatabaseManager
from app.utils import JSONEncoder


class ServiceContainer:
    instance: ServiceContainer | None = None
    db_manager: DatabaseManager | None = None
    json_encoder: JSONEncoder | None = None

    def __new__(cls) -> ServiceContainer:
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def get_db(self) -> DatabaseManager:
        if self.db_manager is None:
            self.db_manager = DatabaseManager()
        return self.db_manager

    def get_json_encoder(self) -> JSONEncoder:
        if self.json_encoder is None:
            self.json_encoder = JSONEncoder()
        return self.json_encoder


def get_db() -> DatabaseManager:
    return ServiceContainer().get_db()


def get_json_encoder() -> JSONEncoder:
    return ServiceContainer().get_json_encoder()
