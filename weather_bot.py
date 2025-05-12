import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import WEATHER_API_KEY, WEATHER_API_URL


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я бот погоды. Используйте /weather <город>, чтобы получить прогноз погоды.")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Доступные команды:\n/start - Приветствие\n/help - Список команд\n/weather <город> - Погода в указанном городе")


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if context.args:
        city = " ".join(context.args)
        params = {
            'q': city,
            'appid': WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'ru'
        }
        response = requests.get(WEATHER_API_URL, params=params)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']
            await update.message.reply_text(
                f"Погода в {city}:\nТемпература: {temperature}°C\nОписание: {weather_description}.")
        else:
            await update.message.reply_text("Не удалось получить данные о погоде. Проверьте название города.")
    else:
        await update.message.reply_text("Пожалуйста, укажите город. Пример: /weather Москва")


def main() -> None:

    application = ApplicationBuilder().token("7544941302:AAHX-9-PTK9BiensyT4cEASNDhViPUyzFLw").build()


    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("weather", weather))


    application.run_polling()

if __name__ == "__main__":
    main()