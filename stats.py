def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if not char in char_dict: char_dict[char] = 0
        char_dict[char] += 1
    return char_dict

def sort_on_num(items):
    return items["num"]

def get_chars_list(char_dict):
    char_list = []
    for char in char_dict:
        char_list.append({"char": char, "num": char_dict[char]})
    char_list.sort(key=sort_on_num, reverse=True)
    return char_list