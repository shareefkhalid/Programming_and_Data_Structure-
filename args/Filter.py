def filter_and_modify(data_list, **kwargs):
 

  filtered_data = []
  for data in data_list:
    
    match = True
    for key, value in kwargs.items():
      
      if callable(value):
        if not value(data.get(key)):
          match = False
          break
      
      elif data.get(key) != value:
        match = False
        break

    
    if match:
      for key, value in kwargs.items():
        if key not in data:
          data[key] = value
      filtered_data.append(data.copy())  

  return filtered_data


data = [
  {"name": "Alice", "age": 30, "city": "New York"},
  {"name": "Bob", "age": 25, "city": "Los Angeles"},
  {"name": "Charlie", "age": 35, "city": "New York"},
  {"name": "Diana", "age": 30, "city": "Chicago"}
]

filtered_data = filter_and_modify(data, age=30, city="New York", occupation="Engineer")
print(filtered_data)
