import requests

BASE_URL = "http://127.0.0.1:5000/books"

def get_books():
    response = requests.get(BASE_URL)
    return response.json()

def get_book(book_id):
    response = requests.get(f"{BASE_URL}/{book_id}")
    return response.json()

def create_book(book_data):
    response = requests.post(BASE_URL, json=book_data)
    return response.json()

def update_book(book_id, book_data):
    response = requests.put(f"{BASE_URL}/{book_id}", json=book_data)
    return response.json()

def delete_book(book_id):
    response = requests.delete(f"{BASE_URL}/{book_id}")
    return response.json()
