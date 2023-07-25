from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



async def choose_lang_btn():
    btn = InlineKeyboardMarkup(row_width=2)
    btn.add(
        InlineKeyboardButton("Uzbek", callback_data="lang_uz"),
        InlineKeyboardButton("Russian", callback_data="lang_ru"),
        InlineKeyboardButton("English", callback_data="lang_en"),
        InlineKeyboardButton("Norwegian", callback_data="lang_no"),
        InlineKeyboardButton("Turkish", callback_data="lang_tr"),
        InlineKeyboardButton("Chinese", callback_data="lang_zh-cn"),
        InlineKeyboardButton("Indonesian", callback_data="lang_id"),
    )
    return btn