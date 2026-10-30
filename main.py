import telebot
from telebot import types

TOKEN = "9227585908:AAHmCfNg9GE7cMcGiEhjJjAQHd1ThXwfbfQ"
bot = telebot.TeleBot(TOKEN)


# /start komandasi uchun menyu
@bot.message_handler(commands=["start"])
def send_welcome(message):
  # Inline tugmalar yaratamiz
  markup = types.InlineKeyboardMarkup(row_width=2)

  btn1 = types.InlineKeyboardButton(
      "🔥 BLATATA PUBG", callback_data="blatata"
  )
  btn2 = types.InlineKeyboardButton(
      "⚡ RUZENN PUBG", callback_data="ruzenn"
  )
  btn3 = types.InlineKeyboardButton(
      "👑 RAMZES PUBG", callback_data="ramzes"
  )
  btn_back = types.InlineKeyboardButton(
      "🔙 Orqaga qaytish", callback_data="back"
  )

  markup.add(btn1, btn2, btn3, btn_back)

  bot.send_message(
      message.chat.id,
      "🤖 **PUBG MOBILE CHUST** botiga xush kelibsiz!\n\n"
      "Marhamat, o'zingizga yoqqan PUBG o'yinchisini tanlang:",
      reply_markup=markup,
      parse_mode="Markdown",
  )


# Tugmalar bosilganda ishlaydigan qism (Callback handler)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
  if call.data == "blatata":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "👑 **BLATATA PUBG** 🥶\n\n"
        "🔹 **CHUST:**\n`1-7638-5041-3477-3578-399`\n\n"
        "🌐 vpn olish uchun: @zuzigbot\n"
        "📢 Nakrutka: @SmmBilanBot",
        parse_mode="Markdown",
    )
  elif call.data == "ruzenn":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "⚡ **RUZENN PUBG** 🥶\n\n"
        "🔹 **UPR:**\n`1-7435-8664-3526-3935-296`\n\n"
        "🔹 **CHUST:**\n`1-7435-8664-3526-3935-297`",
        parse_mode="Markdown",
    )
  elif call.data == "ramzes":
    bot.answer_callback_query(call.id)
    bot.send_message(
        call.message.chat.id,
        "👑 **RAMZES PUBG** haqida ma'lumot tez kunda qo'shiladi!",
    )
  elif call.data == "back":
    bot.answer_callback_query(call.id)
    send_welcome(call.message)


print("Bot ishga tushdi...")
bot.polling()
  
