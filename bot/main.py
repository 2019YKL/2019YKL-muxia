from telegram import Update, InputFile
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
from PIL import Image, ImageDraw, ImageFont
import os

def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="这里是木下狗东西表情包制作平台，欢迎大家使用~")


def add_message_to_image(update: Update, context: CallbackContext, added_message: str):
    # 检查图片文件是否存在
    image_path = '/app/asset/image.png'
    if not os.path.exists(image_path):
        context.bot.send_message(chat_id=update.effective_chat.id, text="找不到图片文件，请检查路径。")
        return

    # 打开图片
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # 设置字体和大小
    font_path = '/app/asset/NotoSansCJKsc-Bold.otf'
    if not os.path.exists(font_path):
        context.bot.send_message(chat_id=update.effective_chat.id, text="找不到字体文件，请检查路径。")
        return
    font = ImageFont.truetype(font_path, 52)

    text_bbox = draw.textbbox((0, 0), added_message, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    # 设置文本颜色为黑色
    text_color = (0, 0, 0)

    # 计算文本的宽度
    text_width, _ = draw.textsize(added_message, font=font)

    # 计算文本的起始X坐标，使其水平居中
    image_width, _ = image.size
    position_x = (image_width - text_width) // 2

    # 将文本添加到图片上
    position = (position_x, 20)
    draw.text(position, added_message, font=font, fill=text_color)

    # 调整图片大小为 256x256 像素
    image = image.resize((256, 256), Image.ANTIALIAS)

    # 保存新图片
    new_image_path = '/app/asset/new_image.png'
    image.save(new_image_path)

    # 发送图片
    with open(new_image_path, 'rb') as f:
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=f)

    return ConversationHandler.END


def muxia(update: Update, context: CallbackContext):
    message_text = update.message.text
    if "/muxia" not in message_text:
        return

    # 提取文本消息
    added_message = message_text.split("/muxia", 1)[1].strip()

    # 条件1：如果文本消息不包含"木下"关键字
    if "木下" not in added_message:
        context.bot.send_message(chat_id=update.effective_chat.id, text="抱歉，只能爱木下一个人哦")
        return

    # 条件2：如果文本消息超过10个汉字
    if len(added_message) > 10:
        context.bot.send_message(chat_id=update.effective_chat.id, text="轻点 木下桑怕疼")
        return

    add_message_to_image(update, context, added_message)


def cancel(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="取消添加消息。")
    return ConversationHandler.END

def main():
    # Get the bot's token from the environment variable
    token = os.environ.get("TELEGRAM_BOT_TOKEN")

    # Create the Updater and pass it your bot's token.
    updater = Updater(token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    # Add command handlers
    dp.add_handler(CommandHandler("muxia", muxia))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()