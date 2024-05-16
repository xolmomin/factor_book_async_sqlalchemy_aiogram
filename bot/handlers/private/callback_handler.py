from aiogram import Router
from aiogram.types import CallbackQuery

callback_router = Router()


@callback_router.callback_query()
async def command_start_handler(callback: CallbackQuery) -> None:
    await callback.answer('xabar', show_alert=True)
