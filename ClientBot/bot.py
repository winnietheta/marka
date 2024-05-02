import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import Config, load_config
from src.handlers import start, marks, open_subject, add_mark, reset_marks, open_mark, delete_mark, import_marks, \
    communities, stuff

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
               "[%(asctime)s] - %(name)s - %(message)s",
    )

    logger.info("Starting bot")

    config: Config = load_config()

    bot: Bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp: Dispatcher = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(marks.router)
    dp.include_router(open_subject.router)
    dp.include_router(add_mark.router)
    dp.include_router(reset_marks.router)
    dp.include_router(open_mark.router)
    dp.include_router(delete_mark.router)
    dp.include_router(import_marks.router)
    dp.include_router(communities.router)
    dp.include_router(stuff.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("Bot stopped")
