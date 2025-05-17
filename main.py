import stats
import sys

# book bot main

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        contents_of_file = f.read()
    return contents_of_file

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {stats.get_num_words(book)} total words")
    print("--------- Character Count -------")
    stats.print_sorted_characters(stats.sort_characters(stats.get_num_characters(book)))
    print("============= END ===============")

main()