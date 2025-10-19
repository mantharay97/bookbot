from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = count_words(text)
    num_char = count_characters(text)
    print(f"Found {num_words} total words")
    print(num_char)

if __name__ == "__main__":
    main()