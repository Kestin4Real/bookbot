from stats import get_word_count, get_char_count, get_chars_list

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    book = get_book_text("books/frankenstein.txt")

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