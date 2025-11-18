__all__ = ['admins_router',]

from aiogram import Router

from .callbacks import callbacks_router
from .messages import messages_router

admins_router = Router()
admins_router.include_routers(callbacks_router, messages_router)