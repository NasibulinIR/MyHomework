import requests
from bs4 import BeautifulSoup
from googletrans import Translator



def get_english_word():
    url = 'https://randomword.com/'
    translator = Translator()
    src_lng = 'auto'
    dest_lng = 'ru'
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find('div', id='random_word').text.strip()
        translated_english_word = translator.translate(english_word, src=src_lng, dest=dest_lng)
        word_definition = soup.find('div', id='random_word_definition').text.strip()
        translated_word_definition = translator.translate(word_definition, src=src_lng, dest=dest_lng)
        return {
            'english_words': translated_english_word.text,
            'word_definition': translated_word_definition.text
        }
    except:
        print('Произошла ошибка')

def word_game():
    print('Добро пожаловать в игру!')
    while True:
        word_dict = get_english_word()
        word = word_dict.get('english_words')
        word_definition = word_dict.get('word_definition')

        print(f'Значение слова - {word_definition}')
        user_input = input('Что это за слово? Введите ответ:')
        if user_input == word:
            print("Все верно!")
        else:
            print(f'Ответ неверный, было загадано слово - {word}')

        play_again = input('Хотите сыграть еще? Введите \'y\' или \'n\':')
        if play_again != 'y':
            print('Спасибо за игру!')
            break

word_game()