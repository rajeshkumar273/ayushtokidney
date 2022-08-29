from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time

chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)

# Training With Own Questions 
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(chatbot)

training_data_quesans = open(r'C:\Users\admin\Desktop\Expert_System\AtoK\training_data\ques_ans.txt').read().splitlines()
training_data_personal = open(r'C:\Users\admin\Desktop\Expert_System\AtoK\training_data\personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer.train(training_data)

# Training With Corpus
from chatterbot.trainers import ChatterBotCorpusTrainer

trainer_corpus = ChatterBotCorpusTrainer(chatbot)

trainer_corpus.train(
    'chatterbot.corpus.english'
)

name=input("Enter your name:")
print("Welcome to Our AtoK_ChaBbot:",name,'Let me know how can i help you?')
while True:
  request=input(name+':')
  if request=='Bye' or request=='bye':
    print("Bot:Bye")
    break
  else:
    response=chatbot.get_response(request)
    print('BOt:',response)



