def get_total_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_dict = {}
    for char in text.lower():
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_character_count(char_dict):
    dict_list = []
    for char, count in char_dict.items():
        dict_list.append({"char": char, "num": count})
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list