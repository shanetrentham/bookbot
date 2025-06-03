from stats import get_word_count
from stats import get_count_of_characters

def get_books_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    # book_content = get_books_text("books/frankenstein.txt")
    word_count = get_word_count("books/frankenstein.txt")
    character_counts = get_count_of_characters("books/frankenstein.txt")
    print(f"{word_count} words found in the document")
    print(character_counts)

main()