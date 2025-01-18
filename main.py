def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_counts = count_letters(text)
    letter_list = list_to_dicts(letter_counts)
    letter_list.sort(reverse=True, key=sort_on)
    
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    print()
    
    for letter in letter_list:
        print(f"The '{letter["name"]}' character was found {letter["num"]} times")

def list_to_dicts(letter_counts):
    return [{"name": key, "num": value} for key, value in letter_counts.items()]

def sort_on(letter_counts):
    return letter_counts["num"]

def count_letters(text):    
    letter_counts = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
    
