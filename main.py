from stats import count_words, count_char, report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main(file_path):
    result = get_book_text(file_path)
    num_words = len(count_words(result))
    print("================ BOOKBOT ================")
    print(f"Found {num_words} total words")
    num_chars = count_char(result)
    report(result)

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main(sys.argv[1])
