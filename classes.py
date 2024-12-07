class Author:
  def __init__(self, name: str, birth_year: int):
    self.name = name
    self.birth_year = birth_year

  def to_dict(self):
    return {
      "AuthorName": self.name,
      "BirthYear": self.birth_year
    }

class Book:
  def __init__(self, title: str, author: Author, genre: str, publication_year: int):
    self.title = title
    self.author = author
    self.genre = genre
    self.publication_year = publication_year
  def to_dict(self):
    return{
      "Title": self.title,
      "Author": self.author.to_dict(),
      "Genre": self.genre,
      "PublicationYear": self.publication_year
    }

class Reader:
  def __init__(self, name:str, age:int, reader_id: int):
    self.name= name
    self.age = age
    self.reader_id = reader_id

  def to_dict(self):
    return{
      "Name":self.name,
      "Age":self.age,
      "ReaderID":self.reader_id
    }
class Librarian:
  def __init__(self, name:str, librarian_id: int):
    self.name = name
    self.librarian_id = librarian_id

  def to_dict(self):
    return{
      "Name": self.name,
      "LibrarianID": self.librarian_id
    }
      
    
    
