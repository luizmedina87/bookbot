from stats import (
  count_words,
  count_characters,
  sort_dict_on_values,
)
import sys

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
  
def print_list(list_of_dict):
  for d in list_of_dict:
    print(f"{d['name']}: {d['count']}")

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  else:
    book_text = get_book_text(sys.argv[1])
    word_count = count_words(book_text)
    char_count_dict = count_characters(book_text.lower())
    sorted_list = sort_dict_on_values(char_count_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_list(sorted_list)

main()