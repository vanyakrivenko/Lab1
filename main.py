from classes import Reader, Librarian, Author, Book
from serializer import JSONSerializer


def main():
  print("Добро пожаловать в систему управления библиотекой!")
  data = []
  serializer = JSONSerializer(data)

  while True:
    print("\nВы хотите создать новый файл или загрузить существующий?")
    print("1. Создать новый файл")
    print("2. Загрузить существующий файл")
    print("3. Выйти из приложения")

    choice = input("Введите номер действия: ")

    if choice == "1":
      data = []
      serializer = JSONSerializer(data)
      print("Новый файл создан.")
      manage_library(data, serializer)

    elif choice == "2":
      file_name = input("Введите название существующего файла (с расширением .json): ")
      try:
        data = serializer.load_from_json(file_name)
        serializer = JSONSerializer(data)
        print("Файл успешно загружен.")
        manage_library(data, serializer)
      except Exception as e:
        print(f"Ошибка при загрузке файла: {e}")
    elif choice == "3":
      print("Выход из приложения До свидания!")
      break
    else:
      print("Неверный выбор. Попробуйте снова.")

def manage_library(data, serializer):
  while True:
    print("\nВыберите действие:")
        print("1. Добавить читателя")
        print("2. Добавить библиотекаря")
        print("3. Добавить книгу")
        print("4. Просмотреть данные")
        print("5. Сохранить данные в файл")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Введите имя читателя: ")
            age = int(input("Введите возраст читателя: "))
            reader_id = int(input("Введите ID читателя: "))
            reader = Reader(name = name, age= age,reader_id=reader_id)
            data.append(reader)
            print("Читатель добавлен.")
        elif choice == "2":
            name = input("Введите имя библиотекаря: ")
            librarian_id=int(input("Введите ID библиотекаря: "))
            librarian = Librarian(name = name, librarian_id = librarian_id)
            data.append(librarian)
            print("Библиотекарь добавлен.")
        elif choice == "3":
            title = input("Введите назване книги: ")
            author_name = input("Введите имя автора: ")
            author_birth_year = int(input("Введите год рождения автора: "))
            genre = input("Введите жанр книги: ")
            publication_year = int(input("Введите год издания книги: "))
            author = Author(name=author_name, birth_year=author_birth_year)
            book = Book(title=title,author = author,genre = genre, publication_year= publication_year)
            data.append(book)
            print("Книга добавлена. ")
        elif choice == "4":
            print("\nДанные библиотеки: ")
            for item in data:
                print(item.to_dict())
        elif choice == "5":
            file_name = input("Введите название файла для сохранения(с раширением .json): ")
            if serializer.save_to_json(file_name):
                print(f"Данные успешно сохранены в файл {file_name}.")
            else:
                print("Ошибка при сохранении файла.")
        elif choice == "6":
            print("Возврат в главное меню.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
  main()



  
  
