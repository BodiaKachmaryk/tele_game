from pymongo import MongoClient

mongodb = "mongodb+srv://bogdankacmarik:Saloz2005@cluster0.kyuy4dj.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(mongodb)
database = client.get_database("telegram_bot_game")
bot_telegram_collection = database.get_collection("bot_telegram")