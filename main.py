import asyncio
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# --- Render porti uchun veb-server (24/7 ishlashi uchun) ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_server, daemon=True).start()
# -----------------------------------------------------------

# Telegram Bot Tokeningiz
TOKEN = "9227585908:AAFo3U1x9FJXekbiAE6GBYdbu-rAAIiteNA"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# YouTube kanal havolasi
YOUTUBE_URL = "https://www.youtube.com/@JOHA_ANIME_UZ"

# 1. /start buyrug'i - Skrinshot talab qilish
@dp.message(Command("start"))
async def start_handler(message: types.Message):
    youtube_keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="▶️ YouTube kanalga o'tish", url=YOUTUBE_URL)]
        ]
    )
    await message.answer(
        "👋 Assalomu alaykum!\n\n"
        "🤖 Botdan foydalanish uchun quyidagi shartni bajaring:\n"
        "1️⃣ YouTube kanalimizga obuna bo'ling.\n"
        "2️⃣ Obuna bo'lganingizni tasdiqlovchi **SKRINSHOT (rasm)** ni shu botga yuboring.\n\n"
        "✨ Shundan so'ng bot avtomatik ishga tushadi!",
        reply_markup=youtube_keyboard
    )

# 2. Xabarlarni tekshirish handler-i
@dp.message()
async def all_messages_handler(message: types.Message):
    # Agar foydalanuvchi rasm yuborgan bo'lsa
    if message.photo:
        main_keyboard = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text="🎮 PUBG Statistika"), KeyboardButton(text="👥 O'yinchilar")],
                [KeyboardButton(text="ℹ️ Yordam")]
            ],
            resize_keyboard=True
        )
        await message.answer(
            "✅ Skrinshot qabul qilindi! Obunangiz tasdiqlandi.\n\n"
            "🎉 CHUST PUBG BOTga xush kelibsiz. Kerakli bo'limni tanlang.",
            reply_markup=main_keyboard
        )
    elif message.text and message.text.startswith("/help"):
        await message.answer("Bu bot orqali siz PUBG o'yini bo'yicha ma'lumotlar olishingiz mumkin.")
    elif message.text == "🎮 PUBG Statistika":
        await message.answer("📊 PUBG statistikasini ko'rish uchun o'yinchi ID raqamini yuboring (Masalan: 123456789).")
    elif message.text == "👥 O'yinchilar":
        await message.answer("👥 Chust o'yinchilari ro'yxati shakllantirilmoqda...")
    elif message.text == "ℹ️ Yordam":
        await message.answer("🛠 Yordam va murojaat uchun adminga yozing:\n📞 Tel: +998945024209")
    elif message.text and message.text.isdigit():
        player_id = message.text
        await message.answer(f"🔍 Qidirilmoqda... PUBG ID: {player_id}\n⚠️ Hozircha baza ulanmagani uchun ma'lumot topilmadi.")
    else:
        await message.answer("⚠️ Iltimos, oldin YouTube kanalga obuna bo'lib, **skrinshot yuboring**!")

# Botni ishga tushirish
async def main():
    print("Bot muvaffaqiyatli ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
      
