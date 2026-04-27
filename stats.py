def count_words(text):
  return len(text.split())

def count_characters(text):
  counts= dict()
  for char in text:
    if char in counts:
      counts[char] += 1
    else:
      counts[char] = 1
  return counts

def sort_on(items):
  return items["count"]

def sort_dict_on_values(dictionary):
  list_of_dict = []
  for k in dictionary:
    list_of_dict.append({"name":k, "count":dictionary[k]})
  list_of_dict.sort(reverse=True, key=sort_on)
  return list_of_dict