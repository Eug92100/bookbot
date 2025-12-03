from stats import get_total_words, get_character_count, sort_character_count

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book_path = "books/frankenstein.txt"
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
