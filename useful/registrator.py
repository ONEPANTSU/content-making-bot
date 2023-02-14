from aiogram import Dispatcher

from handlers.main import main_handlers


def register_handlers(dp: Dispatcher):
    main_handlers.register_main_handlers(dp=dp)