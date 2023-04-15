from flask import Flask
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

app = Flask(__name__)
TOKEN = "5650199850:AAFVpNnH9pLBXQkomn-nJZlBnNucjP4s3sQ"
update=telegram.Update
updater = Updater(TOKEN, use_context=True)

5650199850:AAFVpNnH9pLBXQkomn-nJZlBnNucjP4s3sQ
app = Flask(__name__)

@app.route('/')
def home():
 #   return 'Hello, World!'

@app.route('/test')
def test(update, context):
    chat_id="@1093497662"# msg.sender_chat["username"]
    context.bot.sendMessage(chat_id=chat_id, text="test")
    


@app.route("/5650199850:AAFVpNnH9pLBXQkomn-nJZlBnNucjP4s3sQ", methods=['POST'])
def index(update context):
   
    if request.method == "POST":
        content = json.loads(request.get_data())# #WORKING
       
        #chat_id = request.json["message"]["chat"]["id"]
        chat_id="@1093497662"# msg.sender_chat["username"]
  
        context.bot.sendMessage(chat_id=chat_id, text=str(content))

    return 'ok'
