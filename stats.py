#takes book text and splits it into words and counts them
def get_num_words(text):
    words = text.split()
    return len(words)

#takes book text string and counts letters and adds them to dictionary
def get_chars(text):
    lower_text = text.lower()
    characters = set()
    char_dict = {}
    for char in lower_text:
        if char not in characters:
            characters.add(char)
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

#takes a dictionary of letters and their counts and sorts them
def sort_chars(letters_dict):
    new_list = []
    
    for dict in letters_dict:
        sub_dict = {}
        sub_dict["char"] = dict
        sub_dict["num"] = letters_dict[dict]
        new_list.append(sub_dict)
    def sort_on(items):
        return items["num"]
    new_list.sort(reverse=True, key=sort_on)
    return new_list