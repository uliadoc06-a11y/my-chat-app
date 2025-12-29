import nltk
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize
from flask import Flask, render_template, request, jsonify
import os

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

app = Flask(__name__)

class ChatBot:
    def __init__(self):
        # Define conversation patterns
        self.patterns = [
            (r'привет|привеет|hi|hello|hey', ['Привет! Как дела?', 'Добро пожаловать! Чем я могу помочь?']),
            (r'как дела|how are you|how r u', ['Отлично! Спасибо за вопрос. А ты как?', 'Все хорошо!']),
            (r'как тебя зовут|what is your name|who are you', ['Я ChatBot - ваш личный ассистент!', 'Можешь называть меня ChatBot']),
            (r'спасибо|thanks|thank you', ['Всегда пожалуйста!', 'Рад был помочь!']),
            (r'до свидания|goodbye|bye|exit|quit', ['До встречи!', 'Пока!', 'До свидания!']),
            (r'(.*?) помощь', ['Я могу помочь с ответами на вопросы. Просто спроси меня!', 'Конечно! Что тебя интересует?']),
        ]
    
    def get_response(self, user_input):
        """Generate response based on user input"""
        user_input = user_input.lower()
        
        for pattern, responses in self.patterns:
            import re
            if re.search(pattern, user_input):
                import random
                return random.choice(responses)
        
        return 'Интересный вопрос! К сожалению, я не знаю ответ. Попробуй переформулировать вопрос.'

# Initialize chatbot
chatbot = ChatBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    
    bot_response = chatbot.get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
