from bs4 import BeautifulSoup
import requests

URL = "https://www.goodreads.com/shelf/show/50-books-to-read-before-you-die"
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_book_titles = [book_title.getText() for book_title in soup.find_all(class_="bookTitle")]

with open("books_to_read.txt", "w") as file:
    for book_title in all_book_titles:
        file.write(book_title + "\n")



