def get_num_words(path_to_file):
    """Find the amount of words in a text file"""
    with open(path_to_file) as f:
        words = (f.read()).split()
        num_words = len(words)
    return num_words