import json
from classes import Reader, Librarian, Author, Book


class JSONSerializer:
  def __init__(self,data: list):
    self.data = data

  def save_to_json(self,file_name: str) -> bool:
    try:
      with open(file_name, "w", encoding="utf-8") as f:
        json.dump([item.to_dict() for item in self.data], f, indent = 4, ensure_ascii=False)
      return True
    except Exception as e:
      print(f"Ошибка при сохранении файла: {e}")
      return False
  def load_from_json(self, file_name: str) -> list:
    try:
      with open(file_name, "r", encoding = "utf-8") as f:
        data = json.load(f)
      loaded_data = []
      for item in data:
        if "ReaderID" in item:
          reader = Reader(name=item["Name"], age = item["Age"], reader_id=item["ReaderID"])
          loaded_data.append(reader)
        elif "LibrarianID" in item:
          librarian = Librarian(name=item["Name"], librarian_id = item["LibrarianID"])
          loaded_data.append(librarian)
        elif "Title" in item:
          author_data = item["Author"]
          author = Author(name = author_data["AuthorName"], birth_year = author_data["BirthYear"])
          book = Book(title = item["Title"], author = author, genre = item["Genre"], publication_year = item["PublicationYear"])
          loaded_data.append(book)
      return loaded_data
    except Exception as e:
      print(f"Ошибка при загрузке файла: {e}")
      return []
    
          
  
