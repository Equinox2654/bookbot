# Finds stats for files

def get_num_words(path_to_file):
    """Find the amount of words in a text file"""
    with open(path_to_file) as f:
        words = (f.read()).split()
        num_words = len(words)
    return num_words

# counts the amount of times a number appears in a file

def get_num_characters(path_to_file):
    """Finds the amount of all characters in a text file"""
    characters = {}
    with open(path_to_file) as f:
        file = (f.read()).lower()
        for char in file:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    return characters

# sorts characters dictionary from largest to smallest value

def sort_characters(characters):
    """Sorts the characters dictionary from largest to smallest value"""
    sorted_characters = sorted(characters.items(), key=lambda x: x[1], reverse=True)
    return sorted_characters

# prints sorted characters in a readable format
def print_sorted_characters(sorted_characters):
    """Prints sorted characters in a readable format"""
    for char, count in sorted_characters:
        print(f"{char}: {count}")