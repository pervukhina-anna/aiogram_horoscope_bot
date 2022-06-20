import logging
import sys

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import (
    ContentType,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from api_parse_horosc_bot import get_horoscope
from consts import *


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


# Class for holding user's data (FSM)
class UserData(StatesGroup):
    chosen_zodiac = State()
    chosen_day = State()


@dp.message_handler(
    lambda message: message.text not in AVAILABLE_COMMANDS,
    content_types=ContentType.ANY
)
async def reply_unknown_command(message: types.Message):
    """Reply to unknown command or unknown type of content."""
    await message.reply(
        "Sorry, i don't know what to answer 😥"
        "Please, choose command from this list:\n" + HELP_TEXT
    )


@dp.message_handler(commands='start', )
async def reply_start_msg(message: types.Message):
    """Reply to `/start` command."""
    await message.reply(
        f"Hello, <b>{message.from_user.full_name}</b>! I'm Horoscope Bot!\n"
        f"To get info about my abilities and available commands just "
        f"send me /help command. Or...\n"
        f"Let's look for some /horoscope!",
        parse_mode=types.ParseMode.HTML,
    )


@dp.message_handler(commands='share', )
async def reply_share_msg(message: types.Message):
    """Reply to `/share` command."""
    share_btn = InlineKeyboardMarkup()
    share_btn.add(InlineKeyboardButton(
        text='Horoscope Bot',
        switch_inline_query="Check this bot!")
    )
    await message.reply(text='Sharing link below ⬇', reply_markup=share_btn, )


@dp.message_handler(commands='help', )
async def reply_help_msg(message: types.Message):
    """Reply to `/help` command."""
    await message.reply(
        f"<b>{message.from_user.full_name}</b>! I'm Horoscope Bot!\n"
        f"Check my commands list: \n" + HELP_TEXT,
        parse_mode=types.ParseMode.HTML
    )


@dp.message_handler(commands='horoscope', )
async def reply_horoscope_msg(message: types.Message, ):
    """Reply to `/horoscope` command."""
    await message.reply(
        f"<b>{message.from_user.full_name}</b>! Choose your sign:",
        reply_markup=get_sign_keyboard(),
        parse_mode=types.ParseMode.HTML,
    )
    await UserData.chosen_zodiac.set()


@dp.message_handler(
    state=UserData.chosen_zodiac,
    content_types=ContentType.ANY
)
async def choose_zodiac(message: types.Message, state: FSMContext):
    """Reply to zodiac btn"""
    if message.text not in ZODIACS or message.content_type != ContentType.TEXT:
        await message.reply(
            f"<b>{message.from_user.full_name}</b>!"
            f"Please, choose your sign from keyboard below:",
            reply_markup=get_sign_keyboard(),
            parse_mode=types.ParseMode.HTML,
        )
        return
    await state.update_data(chosen_zodiac=message.text)
    await UserData.chosen_day.set()
    await message.reply(
        text='<b>Choose one of the options:</b>',
        reply_markup=get_day_keyboard(),
        parse_mode=types.ParseMode.HTML
    )


@dp.message_handler(state=UserData.chosen_day, content_types=ContentType.ANY)
async def get_full_parse_data(message: types.Message, state: FSMContext):
    """Reply to day btn and sending final result."""
    if message.text not in DAYS or message.content_type != ContentType.TEXT:
        await message.reply(
            f"<b>{message.from_user.full_name}</b>!"
            f"Please, choose day from keyboard below:",
            reply_markup=get_day_keyboard(),
            parse_mode=types.ParseMode.HTML,
        )
        return
    await state.update_data(chosen_day=message.text[14:])
    data = await state.get_data()
    user_params = (
            ('sign', data['chosen_zodiac'].lower()[0:-2]),
            ('day', data['chosen_day']),
        )
    try:
        horoscope_data = get_horoscope(ENDPOINT, params=user_params)
        await message.reply(
            f'<b>{data["chosen_zodiac"]}'
            f'for {horoscope_data.get("current_date")}: \n</b>'
            f'<b>Horoscope</b> — {horoscope_data.get("description")} \n'
            f'<b>Compatibility</b> — {horoscope_data.get("compatibility")} \n'
            f'<b>Mood</b> — {horoscope_data.get("mood")} \n'
            f'<b>Color</b> — {horoscope_data.get("color")} \n'
            f'<b>Lucky number</b> — {horoscope_data.get("lucky_number")} \n'
            f'<b>Lucky time</b> — {horoscope_data.get("lucky_time")} \n\n'
            f'I want one more /horoscope!',
            parse_mode=types.ParseMode.HTML,
            reply_markup=types.ReplyKeyboardRemove()
        )
    except Exception as error:
        logging.error(f'{error} Endpoint is unreachable')
        await message.reply(
            "I'm sorry, my friend! My magic crystal ball is broken 🥺 "
            "Let's try next time!",
            reply_markup=types.ReplyKeyboardRemove()
        )
        if message.from_user.id != TELEGRAM_CHAT_ID:
            await bot.send_message(
                chat_id=TELEGRAM_CHAT_ID,
                text='Hey, Master! Horoscopes endpoint is unreachable 😣 '
                     'Assistance is required!'
            )
    await state.finish()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format=(
            '%(asctime)s -- %(levelname)s: def %(funcName)s in line #'
            '%(lineno)d, logging message -- "%(message)s" || %(name)s'
        ),
        handlers=[
            logging.StreamHandler(stream=sys.stdout),
        ],
    )
    executor.start_polling(dp, skip_updates=True)
