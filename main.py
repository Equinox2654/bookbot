import stats

# book bot main

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents_of_file = f.read()
    return contents_of_file

def main():
    print(get_book_text("books/frankenstein.txt"))
    print(f"{stats.get_num_words("books/frankenstein.txt")} words found in the document.")
    print("")
    print(f"The different characters found are {stats.get_num_characters("books/frankenstein.txt")}.")

main()