from django.core.management.base import BaseCommand
# from telegram.ext import Updater, CommandHandler
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, \
    MessageHandler, filters, CallbackQueryHandler
from django.conf import settings
import logging


async def start(update, context):
    await update.message.reply_text('Hello! I am your bot.')

class Command(BaseCommand):
    help = 'Run the Telegram bot'
    def handle(self, *args, **options):
        logging.basicConfig(
            filename='/var/log/telegram_bot/log',
            filemode='a',
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

        bot_token = settings.TELEGRAM_TOKEN

        application = ApplicationBuilder().token(bot_token).build()
        start_handler = CommandHandler('start', start)
        application.add_handler(start_handler)
        application.run_polling()


