from classes import Reader, Librarian, Author, Book
from serializer import JSONSerializer


def main():
  print("Добро пожаловать в систему управления библиотекой!")
  data = []
  serializer = None

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

  elif choise == "2":
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
    print("Неверный
  
  
