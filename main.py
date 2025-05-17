import stats

# book bot main

books = {
    "frankenstein": "books/frankenstein.txt",
}

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents_of_file = f.read()
    return contents_of_file

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {books['frankenstein']}")
    print("----------- Word Count ----------")
    print(f"Found {stats.get_num_words(books["frankenstein"])} total words")
    print("--------- Character Count -------")
    stats.print_sorted_characters(stats.sort_characters(stats.get_num_characters(books["frankenstein"])))
    print("============= END ===============")

main()