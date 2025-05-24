import requests
from aiogram import Bot, Dispatcher
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import TOKEN, FOND_API_KEY

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Используйте команду /price <акция> чтобы получить цену.')

async def get_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text('Пожалуйста, укажите тикер акции, например: /price AAPL')
        return
    ticker = context.args[0].upper()
    url = f'https://api.polygon.io/v2/last/trade/{ticker}?apiKey={FOND_API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if 'status' in data and data['status'] == 'NOT_FOUND':
            await update.message.reply_text('Тикер не найден.')
        elif 'last' in data:
            price = data['last']['price']
            await update.message.reply_text(f'Последняя цена {ticker}: ${price}')
        else:
            await update.message.reply_text('Ошибка получения данных.')
    else:
        await update.message.reply_text('Ошибка при обращении к API polygon.io.')

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('price', get_price))
    app.run_polling()

if __name__ == '__main__':
    main()