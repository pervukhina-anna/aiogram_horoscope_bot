import os

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv


load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
ENDPOINT = 'https://aztro.sameerkumar.website/'


HELP_TEXT = (
    "/start — send me this command to get basic info about how i work\n"
    "/help — send this command to get list of available commands\n"
    "/horoscope — send this command to get horoscope\n"
    "/share — i'll send u link to share me with friends\n"
)

ZODIACS = (
    'Aries ♈', 'Taurus ♉', 'Gemini ♊', 'Cancer ♋',
    'Leo ♌', 'Virgo ♍', 'Libra ♎', 'Scorpio ♏',
    'Sagittarius ♐', 'Capricorn ♑', 'Aquarius ♒', 'Pisces ♓',
)

DAYS = ('Horoscope for today', 'Horoscope for tomorrow', )

AVAILABLE_COMMANDS = (
    '/start',
    '/horoscope',
    '/share',
    '/help',
    '/share@horoscopes_robot',
    '/horoscope@horoscopes_robot',
    '/help@horoscopes_robot',
    '/start@horoscopes_robot',
)
                     # + ZODIACS + DAYS


def get_sign_keyboard():
    """Creating keyboard for choosing zodiac sign."""
    zodiac_keyboard = ReplyKeyboardMarkup(selective=True)
    zodiac_buttons = [KeyboardButton(text=sign,) for sign in ZODIACS]
    zodiac_keyboard.add(*zodiac_buttons)
    return zodiac_keyboard


def get_day_keyboard():
    """Creating keyboard for choosing day."""
    day_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    day_buttons = [KeyboardButton(text=chosen_day,) for chosen_day in DAYS]
    day_keyboard.add(*day_buttons)
    return day_keyboard
