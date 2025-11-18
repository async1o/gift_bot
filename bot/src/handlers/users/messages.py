from aiogram import Router, F
from aiogram.types import Message

from src.keyboards.inline import channels_kb

router = Router()

async def in_channels(message: Message):
    user_channel_status = message.bot.get_chat_member('', message.from_user.id)

@router.message(F.text == '/start')
async def start(message: Message):
    await message.bot.send_message(chat_id=message.chat.id,
                                   text='Для получения подарка подпишитесь на эти каналы:',
                                   reply_markup=channels_kb())