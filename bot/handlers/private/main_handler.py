from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message

from db import User

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    user_data = message.from_user.model_dump(include={'id', 'first_name', 'username'})
    await User.create(**user_data)
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")
