__all__ = ['main_router',]

from aiogram import Router

from .users import users_router
from .admins import admins_router

main_router = Router()
main_router.include_routers(admins_router, users_router)