def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    char_counts = get_num_characters(text)
    char_list = convert_dict_to_list(char_counts)
    char_list.sort(reverse=True, key=sort_on)
    
    print(f"""--- Begin report of books/frankenstein.txt ---
          
{num_words} words found in the document
""")
    
    for char_dict in char_list:
          print(f"The '{char_dict['name']}' character was found {char_dict['num']} times")
    
    print("""
--- End report ---""")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    char_counts = {}
    for char in text:
        char = char.lower()
        if char.isalpha():
            if char not in char_counts:
                char_counts[char] = 1
            else:
                char_counts[char] += 1
    return char_counts

def convert_dict_to_list(char_counts):
    char_list = []
    for char, count in char_counts.items():
        char_dict = {"name": char, "num": count}
        char_list.append(char_dict)
    return char_list

def sort_on(dict):
    return dict["num"]

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
