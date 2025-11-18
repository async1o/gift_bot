__all__ = ['users_router',]

from aiogram import Router

from .callbacks import router as callbacks_router
from .messages import router as messages_router

users_router = Router()
users_router.include_routers(callbacks_router, messages_router)