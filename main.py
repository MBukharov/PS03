import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_word():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "word": word,
            "word_definition": word_definition
        }
    except:
        return "Что-то пошло не так"

def translate_word(word_data):
    translator = Translator()
    word = word_data.get("word")
    word = translator.translate(word, dest="ru").text
    definition = word_data.get("word_definition")
    definition = translator.translate(definition, dest="ru").text
    return {
        "word": word,
        "word_definition": definition
    }

def game():
    print("Добро пожаловать в игру")
    while True:
        word_data = translate_word(get_word())
        word = word_data.get("word")
        definition = word_data.get("word_definition")

        print(f"\nЗначение слова - {definition}")
        user = input("Что это за слово?\n")

        if user == word:
            print("Верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {word}")

        play_again = input("Хотите сыграть еще раз? да/нет\n")
        if play_again != "да":
            print("Спасибо за игру!")
            break

game()