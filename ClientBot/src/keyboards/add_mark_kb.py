from datetime import datetime
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def make(marks_list):
    kb = ReplyKeyboardBuilder()

    if len(marks_list) > 0:
        for key, value in marks_list.items():
            kb.button(text=key)
    else:
        kb.button(text='Нет предметов для отображения')

    kb.adjust(3)

    return kb


def marks():
    kb = ReplyKeyboardBuilder()

    kb.button(text='5')
    kb.button(text='4')
    kb.button(text='3')
    kb.button(text='2')
    kb.button(text='1')

    kb.adjust(5)

    return kb


def dates():
    kb = ReplyKeyboardBuilder()
    kb.button(text=datetime.now().strftime("%d.%m.%Y"))
    return kb
