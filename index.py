from flask import Flask
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

app = Flask(__name__)
TOKEN = "5650199850:AAFVpNnH9pLBXQkomn-nJZlBnNucjP4s3sQ"
update=telegram.Update
updater = Updater(TOKEN, use_context=True)
bot=telegram.Bot(TOKEN)


@app.route('/')
def home():
   return 'Hello, World!'

app.route('/test')
def test():
  # chat_id="@1093497662"# msg.sender_chat["username"]
   #bot.sendMessage(chat_id=chat_id, text="test")
   return "Done"
    


@app.route("/hook", methods=['POST', "GET"])
def hook():
   if request.method == "POST":
       content = json.loads(request.get_data())# #WORKING
       
        #chat_id = request.json["message"]["chat"]["id"]
       chat_id="@1093497662"# msg.sender_chat["username"]
       bot.sendMessage(chat_id=chat_id, text=str(content))
       return 'ok'
