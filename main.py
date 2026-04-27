from stats import count_words, count_characters, sort_dict_on_values

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents
  
def print_list(list_of_dict):
  for d in list_of_dict:
    print(f"{d['name']}: {d['count']}")

def main():
  book_text = get_book_text("./books/frankenstein.txt")
  word_count = count_words(book_text)
  char_count_dict = count_characters(book_text.lower())
  print(f"Found {word_count} total words")
  print_list(sort_dict_on_values(char_count_dict))

main()