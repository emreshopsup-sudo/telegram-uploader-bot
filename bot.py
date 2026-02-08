from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "7943526075:AAFrzyc4-qNo79rRfyS-M1Thoy6UhsXGNl4"

async def upload(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    if msg.document:
        await msg.reply_document(document=msg.document.file_id)
    elif msg.video:
        await msg.reply_video(video=msg.video.file_id)
    elif msg.audio:
        await msg.reply_audio(audio=msg.audio.file_id)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, upload))
app.run_polling()
