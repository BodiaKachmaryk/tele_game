
import logging
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

state = 1

#TO_ONE_GOAL_BOT

updater = Updater(token="5585661483:AAESAKtCJ6gejn6h6HYoH2mqt3ExzsMr2Gs", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    global state
    
    if state == 1:
        text = """
        Рефері дає свисток, матч розпочався. Твої подальші дії:
        1: Розводить м'яч суперник твоєї команди
        2: Розводить м'яч твоя команда 
        """
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        state += 1
    else:
        pass

def text_message_handler(update: Update, context: CallbackContext):
    message = update.message.text
    global state
    

    if state == 2:

        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            М'яч в команди суперника
            """)
            state = 1
            text = """
            Потрібно відібрати м'яч. 
            Введіть /start, щоб знову вибрати хто буде розводити м'яч з середини поля.
            """
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

        elif message == "2":
            text = """
            Потрібно віддати пас, наступні твої дії:
            1: Віддати пас на цз
            2: Віддати пас на пз
            3: Віддати пас на лз
            """
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            state += 1


    elif state == 3:

        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Ви отримали пас. Наступні Ваші дії з м'ячом:
            1: Розпочати атаку, віддавши дальній пас на товариша
            2: Розпасуватися з воротарем
            3: Віддати пас на ближнього гравця
            """)
            state += 1

        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Ви отримали пас. Наступні Ваші дії з м'ячом:
            1: Розпочати атаку, віддавши дальній пас на товариша
            2: Розпасуватися з воротарем
            3: Віддати пас на ближнього гравця
            """)
            state += 1

        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Ви отримали пас. Наступні Ваші дії з м'ячом:
            1: Розпочати атаку, віддавши дальній пас на нападника
            2: Розпасуватися з воротарем
            3: Віддати пас на ближнього гравця
            """)
            state += 1


    elif state == 4:
        
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text=""" 
            Ви отримали пас. Наступні Ваші дії з м'ячом:
            1: Зробити асист
            2: Вдарити мимо ворі
            """)
            state += 1

        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Ви отримали пас. Наступні Ваші дії з м'ячом:
            1: Віддати пас нападнику
            """)
            state += 1

        elif message == "3":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Ви отримали пас. Наступні Ваші дії з м'ячом:
            1: Віддати пас нападнику
            """)
            state += 1


    elif state == 5:

        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Ви отримали пас. Наступні Ваші дії з м'ячом:
            1: Забити гол
            """)
            state += 1

        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Ви вдарили мимо воріт. 
            """)
            state = 1
            text = "Потрібно знову розвести м'яч. Введіть /start, щоб почати знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)


    elif state == 6:

        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Вітю, Ви забили гол! 
            """)
            state = 1
            text = "Ваша команда перемогла. Введіть /start, щоб почати матч знову."
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()