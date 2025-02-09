import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().split()
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return []

def count_words(words):
    word_counts = {}
    for word in words:
        if word.isalpha():
            if word not in word_counts:
                word_counts[word] = 1
            else:
                word_counts[word] += 1
    return word_counts

def sort_word_counts(word_counts):
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

def get_top_words(sorted_words, top_n=10):
    return sorted_words[:top_n]

def main():
    file_path = 'filter_words.txt'
    
    # Resolve file path relative to the script's directory
    file_path = os.path.join(os.path.dirname(__file__), file_path)
    
    words = read_file(file_path)
    if not words:  # Exit if the file couldn't be read
        return
    
    word_counts = count_words(words)
    sorted_words = sort_word_counts(word_counts)
    top_words = get_top_words(sorted_words)

    print("Top words by frequency:")
    for word, count in top_words:
        print(word, count)

if __name__ == "__main__":
    main()
