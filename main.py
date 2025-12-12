from stats import get_total_words, get_character_count, sort_character_count
import sys

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    text = get_book_text(book_path)
    total_words = get_total_words(text)
    print("--------- Word Count -------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    char_count = get_character_count(text)
    char_dict_list = sort_character_count(char_count)
    for item in char_dict_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")



main()
