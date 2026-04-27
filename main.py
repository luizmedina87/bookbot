def count_words(text):
  return len(text.split())

def get_book_text(filepath):
  with open(filepath) as f:
    file_contents = f.read()
    return file_contents

def main():
  book_text = get_book_text("./books/frankenstein.txt")
  word_count = count_words(book_text)
  print(f"Found {word_count} total words")

main()