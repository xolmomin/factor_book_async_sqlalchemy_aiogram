from aiogram import Router, html, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db import User, Category

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message, bot: Bot) -> None:
    user_data = message.from_user.model_dump(include={'id', 'first_name', 'last_name', 'username'})
    if not await User.get(message.from_user.id):
        await User.create(**user_data)

    categories = await Category.get_all()
    ikb = InlineKeyboardBuilder()
    for category in categories:
        ikb.add(InlineKeyboardButton(text=category.name, callback_data=f'category_{category.id}'))
    ikb.adjust(2, repeat=True)

    await message.answer("Category ni tanlang", reply_markup=ikb.as_markup())
