from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

portuguese_bot = ChatBot(
                 "Chatterbot",
                  storage_adapter="chatterbot.storage.SQLStorageAdapter",
                  logic_adapters=[
                    'chatterbot.logic.BestMatch',
                    {
                        'import_path': 'chatterbot.logic.LowConfidenceAdapter',
                        'threshold': 0.65,
                        'default_response': 'Desculpa, eu não entendi!'
                    }
                  ])

portuguese_bot.set_trainer(ChatterBotCorpusTrainer)

portuguese_bot.train("chatterbot.corpus.portuguese")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(portuguese_bot.get_response(userText))
if __name__ == "__main__":
    app.run()
