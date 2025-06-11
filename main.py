from stats import get_word_count
from stats import get_count_of_characters
from stats import sort_dictionary
import sys

def get_books_text(file_path):
    file_contents = ""
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_books_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    word_count = get_word_count(text)
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    character_counts = get_count_of_characters(text)
    sorted = sort_dictionary(character_counts)
    for k in sorted:
        print(f"{k[0]}: {k[1]}")

main()