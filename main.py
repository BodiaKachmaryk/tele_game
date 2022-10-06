import logging
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater, MessageHandler, Filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# States
START = 1
QUESTION_1 = 2
QUESTION_2 = 3
END = 4

user_states = {}

updater = Updater(token="5689428489:AAHZCYxzZe1cvcRMoxhIdPjsfx0VSN8lGVQ", use_context=True)
dispatcher = updater.dispatcher

def start_command_handler(update: Update, context: CallbackContext):
    global user_states
    
    user_id = update.effective_chat.id
    
    # If user not in states - add him / her
    if user_id not in user_states:
        user_states[user_id] = START
        
    print(f"[/start]: current user state: {user_states[user_id]}")
        
    # Check state of current user
    if user_states[user_id] == START:
        text = """"
Рефері дає свисток, матч почався. 
1: Розводимо м'яч з середини поля
2: М'яч розводить команда суперника
"""
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        user_states[user_id] += 1
    else:
       pass

def text_message_handler(update: Update, context: CallbackContext):
    message = update.message.text
    user_id = update.effective_chat.id
    
    global user_states
    
    print(f"[text]: current user state: {user_states[user_id]}")
    
    if user_states[user_id] == QUESTION_1:
        #if message == "1":
            #context.bot.send_message(chat_id=update.effective_chat.id, text="Хороший вибір")
            #user_states[user_id] = 1
            #text = "Гра закінчилась. Введіть /start, щоб почати знову."
            #context.bot.send_message(chat_id=update.effective_chat.id, text=text)
        if message == "1":
            text = """
            Потрібно віддати пас гравцю своєї команди
            1: Віддати пас на лівий фланг
            2: Віддати пас на правий фланг
            3: Розіграти з ближнім гравцем 
            """
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
            if message == "1":
                context.bot.send_message(chat_id=update.effective_chat.id, text="""
                Наступні твої дії
                1: Розпочати атаку, віддавши дальній пас на товариша
                2: Розпасуватися з воротарем
                3: Віддати пас на ближнього гравця
                """)
                user_states[user_id] += 1
                if message == "1":
                    context.bot.send_message(chat_id=update.effective_chat.id, text="""
                    Наступні твої дії
                    1: Зробити асист
                    2: Вдарити мимо воріт""")
                    if message == "1":
                        context.bot.send_message(chat_id=update.effective_chat.id, text="""
                        Наступні твої дії
                        1: Забити гол""")
                    elif message == "1":
                        context.bot.send_message(chat_id=update.effective_chat.id, text="""
                        Наступні твої дії
                        1: Відібрати м'яч""")
                elif message == "2":
                    context.bot.send_message(chat_id=update.effective_chat.id, text="""
                    Наступні твої дії
                    1: Віддати пас нападнику""")
            elif message == "2":
                context.bot.send_message(chat_id=update.effective_chat.id, text="""
                Наступні твої дії
                1: Розпочати атаку, віддавши дальній пас на товариша
                2: Розпасуватися з воротарем
                3: Віддати пас на ближнього гравця
                """)
                user_states[user_id] += 1
            elif message == "1":
                context.bot.send_message(chat_id=update.effective_chat.id, text="""
                Наступні твої дії
                1: Розпочати атаку, віддавши дальній пас на товариша
                2: Розпасуватися з воротарем
                3: Віддати пас на ближнього гравця
                """)
                user_states[user_id] += 1

        if message == "2":
            text = """
            Потрібно забрати м'яч в команди супреника.
            1: Пресинг суперника
            2: Зачекати поки команда суперника помилиться
            """
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            user_states[user_id] += 1
            if message == "1":
                text = "Чудово, м'яч тепер під контролем твоїх команди"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            elif message =="2":
                text = "Чудово, м'яч тепер під контролем твоїх команди"
                context.bot.send_message(chat_id=update.effective_chat.id, text=text)
            

    elif user_states[user_id] == QUESTION_2:
        if message == "1":
            context.bot.send_message(chat_id=update.effective_chat.id, text="""
            Наступні твої дії
            1: Розпочати атаку, віддавши дальній пас на товариша
            2: Розпасуватися з воротарем
            3: Віддати пас на ближнього гравця
            """)
            user_states[user_id] += 1
        elif message == "2":
            context.bot.send_message(chat_id=update.effective_chat.id, text="Послизнувся і вмер. Бадум тсс...")
            user_states[user_id] += 1
    elif user_states[user_id] == END:
        user_states[user_id] = 1
        text = "Гра закінчилась. Введіть /start, щоб почати знову."
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)
    else:
        pass

start_handler = CommandHandler('start', start_command_handler)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & ~Filters.command, text_message_handler)
dispatcher.add_handler(echo_handler)

# Start bot
updater.start_polling()