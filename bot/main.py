import logging
import asyncio

from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties

from src.utils.settings import settings
from src.handlers import main_router

logging.basicConfig(level=logging.INFO)
logger = logging.Logger(__name__)


async def main():
    session = AiohttpSession()
    bot = Bot(
        token=settings.BOT_TOKEN,
        session=session,
        default=DefaultBotProperties(parse_mode='HTML')
    )

    dp = Dispatcher()
    dp.include_router(main_router)
    try:
        await dp.start_polling(bot)

    except ValueError as e:
        logger.error('ValueError occured: %s: ', e)
    except KeyError as e:
        logger.error("KeyError occured: %s: ", e)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())