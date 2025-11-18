from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from src.utils.settings import settings

async def channels_kb() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()

    channels = settings.CHANNELS.split(',')

    for channel in channels:
        markup.add(InlineKeyboardButton(text='Подписаться', url=f't.me/%s'.format(channel)))

    return markup

