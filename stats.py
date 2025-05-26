def get_num_words(text):
        file_count = len(text.split())
        return file_count

def get_num_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(dict):
    return dict["num"]

def sorted_dict(dict):
    new_dict = []
    for char, num in dict.items():
        dict_guide = {"char": char, "num": num}
        new_dict.append(dict_guide)
    
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict


