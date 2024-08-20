def search_replace(my_list, search, replace):
  new_list = []
  for item in my_list:
    if item == search:
      new_list.append(replace)
    else:
      new_list.append(item)
  return new_list

my_list = [1, 2, 3, 4, 5, 2, 1, 1, 4, 89]
new_list = search_replace(my_list, 2, 89)

print(my_list)
print(new_list)
