from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardButton, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from db import Product

callback_router = Router()


@callback_router.callback_query(F.data.startswith('category_'))
async def category_callback_handler(callback: CallbackQuery) -> None:
    category_id = int(callback.data.split('category_')[-1])
    products = await Product.get_products_by_category_id(category_id)

    ikb = InlineKeyboardBuilder()
    for product in products:
        ikb.add(InlineKeyboardButton(text=product.name, callback_data=f'product_{product.id}'))
    ikb.adjust(3, repeat=True)

    await callback.message.edit_text('Productni tanlang 📚', reply_markup=ikb.as_markup())


@callback_router.callback_query(F.data.startswith('product_'))
async def command_start_handler(callback: CallbackQuery) -> None:
    product_id = int(callback.data.split('product_')[-1])
    product = await Product.get(product_id)
    await callback.message.delete()
    await callback.message.answer_photo(URLInputFile(product.photo.telegra_image_url), product.name)
    await callback.answer(f"{product_id} tanlandi", show_alert=True)
