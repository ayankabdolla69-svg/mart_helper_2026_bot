import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load--dotenv  # Если используешь .env файл

# Загружаем переменные окружения (если используется файл .env)
load_dotenv()

# Получаем токен из переменных окружения
BOT_TOKEN = os.getenv("8612210288:AAH2wVYMh5M8TGI5zpn4FcQ5HQJ-NLOQ29A")

if not BOT_TOKEN:
    raise ValueError("8612210288:AAH2wVYMh5M8TGI5zpn4FcQ5HQJ-NLOQ29A")

# Инициализируем бота и диспетчер
bot = Bot(token="8612210288:AAH2wVYMh5M8TGI5zpn4FcQ5HQJ-NLOQ29A")
dp = Dispatcher()

# Создаем клавиатуру с кнопками (Reply-клавиатура)
def get_main_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="📌 О нас"), KeyboardButton(text="🎯 Направления")],
        [KeyboardButton(text="📞 Контакты")]
    ]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

# Обработчик команды /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    welcome_text = (
        f"Здравствуйте, {message.from_user.first_name}! 👋\n\n"
        "Добро пожаловать в официальный бот Молодёжного ресурсного центра. "
        "Здесь вы можете узнать основную информацию о нашей деятельности, направлениях работы и связаться с нами.\n\n"
        "Выберите интересующий вас раздел с помощью кнопок ниже:"
    )
    await message.answer(welcome_text, reply_markup=get_main_keyboard())

# Обработчик кнопки "📌 О нас"
@dp.message(F.text == "📌 О нас")
async def about_us(message: types.Message):
    text = (
        "<b>📌 О Молодёжном ресурсном центре:</b>\n\n"
        "Мы работаем для поддержки инициатив молодёжи, помощи в самореализации, "
        "консультирования по различным вопросам, а также организации социально значимых, "
        "культурных и спортивных мероприятий."
    )
    await message.answer(text, parse_mode="HTML")

# Обработчик кнопки "🎯 Направления"
@dp.message(F.text == "🎯 Направления")
async def directions(message: types.Message):
    text = (
        "<b>🎯 Основные направления нашей работы:</b>\n\n"
        "1. <b>Волонтёрство</b> — развитие добровольческого движения и помощь в организации акций.\n"
        "2. <b>Молодёжные инициативы</b> — поддержка и реализация полезных проектов.\n"
        "3. <b>Информационная работа</b> — освещение событий, грантовых программ и возможностей для молодёжи.\n"
        "4. <b>Консультирование</b> — помощь молодым специалистам и студентам."
    )
    await message.answer(text, parse_mode="HTML")

# Обработчик кнопки "📞 Контакты"
@dp.message(F.text == "📞 Контакты")
async def contacts(message: types.Message):
    text = (
        "<b>📞 Наши контакты:</b>\n\n"
        "📍 <b>Адрес:</b> ул. Примерная, д. 1\n"
        "📞 <b>Телефон:</b> +7 (XXX) XXX-XX-XX\n"
        "📧 <b>Email:</b> mrc_example@mail.kz\n"
        "⏰ <b>График работы:</b> Понедельник – Пятница, с 09:00 до 18:30"
    )
    await message.answer(text, parse_mode="HTML")

# Главная функция для запуска бота
async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот успешно запущен и ожидает сообщения...")
    # Удаляем вебхуки на случай старых зависших запросов и запускаем поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
