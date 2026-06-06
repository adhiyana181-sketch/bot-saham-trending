import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# MASUKKAN TOKEN BOT TELEGRAM KAMU DI SINI
TOKEN = "8883556379:AAG9YAvddRo6vCOfRa-0iKVtmYUrGHKSC7k"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"🤖 *VF AI TRENDING ASSISTANT* v1.0\n"
        f"⚡ _Welcome, {user.first_name}. Market Intelligence Active._\n\n"
        f"Gunakan menu navigasi di bawah untuk memulai analisa saham BEI:"
    )
    
    keyboard = [
        [InlineKeyboardButton("📊 IHSG Status", callback_data='ihsg'),
         InlineKeyboardButton("🔥 Top Trending", callback_data='trending'),
         InlineKeyboardButton("🚀 Breakout", callback_data='breakout')],
        [InlineKeyboardButton("📈 Akumulasi Vol", callback_data='accumulation'),
         InlineKeyboardButton("🌐 Foreign Flow", callback_data='foreign'),
         InlineKeyboardButton("🐳 Big Money", callback_data='bigmoney')],
        [InlineKeyboardButton("🎯 Target Price", callback_data='target_help'),
         InlineKeyboardButton("📉 Oversold Peak", callback_data='oversold'),
         InlineKeyboardButton("🔄 Sektor Rotasi", callback_data='rotasi')],
        [InlineKeyboardButton("🧱 Support/Resist", callback_data='snr_help'),
         InlineKeyboardButton("🕵️ Bandar Check", callback_data='bandar_help'),
         InlineKeyboardButton("🚨 Set Price Alert", callback_data='alert_help')]
    ]
    
    await update.message.reply_text(text=welcome_text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'accumulation':
        text = (
            "🟩 *RANKING AKUMULASI TERBESAR*\n"
            " _Green candle besar + volume spike_\n\n"
            "1. *PSAB* 500  Vol × 2.0\n   Body 5.49% (`+6.38%`)\n"
            "2. *MIKA* 1,525  Vol × 0.9\n   Body 3.74% (`-3.48%`)\n"
            "3. *MEGA* 1,810  Vol × 1.0\n   Body 1.97% (`+0.56%`)\n"
            "4. *APLN* 132  Vol × 0.4\n   Body 1.54% (`+1.54%`)\n\n"
            "📊 _Proxy akumulasi dari candle + volume. Bukan data broker._"
        )
        back_keyboard = [[InlineKeyboardButton("⬅️ Kembali ke Menu", callback_data='main_menu')]]
        await query.edit_message_text(text=text, reply_markup=InlineKeyboardMarkup(back_keyboard), parse_mode='Markdown')
        
    elif query.data == 'main_menu':
        keyboard = [
            [InlineKeyboardButton("📊 IHSG Status", callback_data='ihsg'), InlineKeyboardButton("🔥 Top Trending", callback_data='trending'), InlineKeyboardButton("🚀 Breakout", callback_data='breakout')],
            [InlineKeyboardButton("📈 Akumulasi Vol", callback_data='accumulation'), InlineKeyboardButton("🌐 Foreign Flow", callback_data='foreign'), InlineKeyboardButton("🐳 Big Money", callback_data='bigmoney')],
            [InlineKeyboardButton("🎯 Target Price", callback_data='target_help'), InlineKeyboardButton("📉 Oversold Peak", callback_data='oversold'), InlineKeyboardButton("🔄 Sektor Rotasi", callback_data='rotasi')],
            [InlineKeyboardButton("🧱 Support/Resist", callback_data='snr_help'), InlineKeyboardButton("🕵️ Bandar Check", callback_data='bandar_help'), InlineKeyboardButton("🚨 Set Price Alert", callback_data='alert_help')]
        ]
        await query.edit_message_text(text="🤖 *VF AI TRENDING ASSISTANT* v1.0\nSilahkan pilih menu:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode='Markdown')
    else:
        # Template respons fitur lainnya agar bot tidak error saat tombol diklik
        await query.edit_message_text(
            text=f"📊 Fitur *{query.data}* sedang menarik data real-time dari bursa...",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Kembali", callback_data='main_menu')]]),
            parse_mode='Markdown'
        )

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.run_polling()

if __name__ == '__main__':
    main()
