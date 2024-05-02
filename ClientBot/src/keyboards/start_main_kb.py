from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def make():
    builder = InlineKeyboardBuilder()

    builder.row(InlineKeyboardButton(text='⚡️ Мои оценки', callback_data='marks'))
    builder.row(InlineKeyboardButton(text='📦 Перенести оценки', callback_data='import_marks'))
    builder.row(InlineKeyboardButton(text='👨‍💻 Сообщества', callback_data='communities'))
    builder.row(InlineKeyboardButton(text='👥 Полезные материалы', callback_data='stuff'))

    return builder
