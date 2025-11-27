# Task 2: Inventory Manager

import json
from pathlib import Path
from book import Book
import logging

# Logging setup
logging.basicConfig(filename="library.log",
                    level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

class LibraryInventory:
    def __init__(self, file_path="books.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load()

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Book added: {book}")

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        if not self.books:
            print("No books in library.")
        else:
            for b in self.books:
                print(b)

    # ---------- Task 3: File Persistence ----------
    def save(self):
        try:
            data = [b.to_dict() for b in self.books]
            with open(self.file_path, "w") as f:
                json.dump(data, f, indent=4)
                logging.info("Catalog saved successfully.")
        except Exception as e:
            logging.error(f"Error saving file: {e}")

    def load(self):
        try:
            if self.file_path.exists():
                with open(self.file_path, "r") as f:
                    data = json.load(f)
                    self.books = [Book.from_dict(d) for d in data]
                    logging.info("Catalog loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading file: {e}")
            print("Error reading file. Starting with empty library.")
            self.books = []
