from stats import get_num_words

# book bot main

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents_of_file = f.read()
    return contents_of_file

def main():
    print(get_book_text("books/frankenstein.txt"))
    print(f"{get_num_words("books/frankenstein.txt")} words found in the document.")

main()