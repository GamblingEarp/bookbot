import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit

def main():
    try:
        book_path = sys.argv[1]
    except Exception as e:
        print(f"Error encountered: {e}")
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_chars(text)
    sorted_chars = sort_chars(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for char in sorted_chars:
        character = char["char"]
        if character.isalpha():
            print(f"{char["char"]}: {char["num"]}")

    print("============= END ===============")


#contents of file into a string
def get_book_text(path):
    with open(path) as f:
        return f.read()

from stats import get_num_words
from stats import get_chars
from stats import sort_chars

main()
