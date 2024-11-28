import string

def word_count(book):
    words_list = book.split()
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words_list)} words found in the document\n")


def count_character(book):
    book = book.lower()    
    char_count = {}

    for ch in range(ord('a'), ord('z') + 1):
        char_count[chr(ch)] = 0
    
    for ch in book:
        if ch.isalpha():
            char_count[ch] += 1
    
    char_occurance = sorted(char_count.items(), key=lambda item: item[1], reverse=True)
    for char, count in char_occurance:
        print(f"The {char} character was found {count} times")



def main():
    file_path = 'books/frankenstein.txt'
    with open(file_path, 'r', encoding='utf-8') as f:
        file_contents = f.read() 

        word_count(file_contents)
        count_character(file_contents) 

if __name__ == "__main__":
    main()
