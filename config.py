import os
from dataclasses import dataclass, asdict

from dotenv import load_dotenv

load_dotenv()


@dataclass
class BaseConfig:
    def asdict(self):
        return asdict(self)


@dataclass
class DatabaseConfig(BaseConfig):
    """Database connection variables"""
    NAME: str = os.getenv('DB_NAME')
    USER: str = os.getenv('DB_USER')
    PASSWD: str = os.getenv('DB_PASSWORD')
    HOST: str = os.getenv('DB_HOST')
    PORT: str = os.getenv('DB_PORT')

    @property
    def db_url(self):
        return f"postgresql+asyncpg://{self.USER}:{self.PASSWD}@{self.HOST}:{self.PORT}/{self.NAME}"


@dataclass
class BotConfig(BaseConfig):
    """Bot configuration"""
    BASE_URL: str = os.getenv('BASE_URL')
    BOT_TOKEN: str = os.getenv('BOT_TOKEN')
    ADMIN_LIST: str = os.getenv('ADMIN_LIST')

    WEB_SERVER_HOST: str = os.getenv('WEB_SERVER_HOST')
    WEB_SERVER_PORT: int = int(os.getenv('WEB_SERVER_PORT', 8080))
    WEBHOOK_PATH = "/webhook"
    WEBHOOK_SECRET = os.getenv('WEBHOOK_SECRET')
    BASE_WEBHOOK_URL = os.getenv('BASE_WEBHOOK_URL')

    # MAIN_BOT_PATH: str = "/webhook/main"
    # OTHER_BOTS_PATH: str = "/webhook/bot/{bot_token}"
    #
    # OTHER_BOTS_URL: str = f"{BASE_URL}{OTHER_BOTS_PATH}"

    @property
    def get_admin_list(self):
        return list(map(int, self.ADMIN_LIST.split(',')))


@dataclass
class Configuration:
    """All in one configuration's class"""
    db = DatabaseConfig()
    bot = BotConfig()


conf = Configuration()
