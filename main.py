import sys
from stats import get_word_count, get_char_count, get_chars_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    book = get_book_text(path)

    print("----------- Word Count ----------")
    words = get_word_count(book)
    print(f"Found {words} total words")

    print("--------- Character Count -------")
    char_dict = get_char_count(book)
    char_list = get_chars_list(char_dict)
    for dict in char_list:
        if dict["char"].isalpha(): print(f"{dict["char"]}: {dict["num"]}")

    print("============= END ===============")

main()