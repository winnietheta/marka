from dataclasses import dataclass

from dotenv import load_dotenv

from .base import getenv


@dataclass
class TelegramBotConfig:
    token: str


@dataclass
class Config:
    tg_bot: TelegramBotConfig


def load_config() -> Config:
    # Parse a `.env` file and load the variables into environment variables
    load_dotenv()

    return Config(tg_bot=TelegramBotConfig(token=getenv("BOT_TOKEN")))
