import json


PATH = "notebooks.json"


def save_json(path, book):
    books = load_json(path)
    books.insert(0, book)
    with open(path, "w", encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False)


def replace_from_json(path, i):
    books = load_json(path)
    book = books[i]
    del books[i]
    books.insert(0, book)
    with open(path, "w", encoding='utf-8') as file:
        json.dump(books, file, ensure_ascii=False)


def load_json(path):
    with open(path, "r", encoding='utf-8') as file:
        return json.load(file)


def set_book(book_text):
    return {"text": book_text}


def main():
    print("Что вы хотите?\n"
          "1. Добавить заметку\n"
          "2. Посмотреть заметки\n"
          "3. Выйти")
    user_input = int(input())
    if user_input == 3:
        quit()
    elif user_input == 1:
        text = input(f"Это твой блокнот на день\n"
                     f"запиши все что ты планируешь")
        save_json(PATH, set_book(text))
    elif user_input == 2:
        books = load_json(PATH)
        for i in range(len(books)):
            print(f"{i + 1}: {books[i]['text']}\n"
                  f"{books[i]['date']}")
        user_input = int(input("0. Выход\n"
                               "Индекс для перемещения"))
        if user_input == 0:
            quit()
        replace_from_json(PATH, user_input - 1)


if __name__ == "__main__":
    main()
