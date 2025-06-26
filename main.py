from stats import count_words, count_char, report

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    result = get_book_text("./books/frankenstein.txt")
    num_words = len(count_words(result))
    print(f"Found {num_words} total words")
    num_chars = count_char(result)
    report(result)

main()
