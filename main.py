def main():
    book_path = "/root/workspace/github.com/vjmill/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = count_characters(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print_report(char_dict)
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()  
    char_dict = {}
    for char in text:  
         if char not in char_dict:
                char_dict[char] = 1
         else:
                char_dict[char] += 1
    return char_dict

def print_report(char_dict):
     char_only_dict = {}
     for char in char_dict:
          if char.isalpha():
               char_only_dict[char] = char_dict[char]
     for char in char_only_dict:
          print(f"The '{char}' character was found {char_only_dict[char]} times")
        
def get_book_text(path):
    with open(path) as f:
        return f.read()


main()