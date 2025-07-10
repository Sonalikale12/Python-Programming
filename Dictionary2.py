# Create a dictionary by extracting the keys from a given dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
dict2= {a: sample_dict[a] for a in keys}
print(dict2)

# Delete a list of keys from a dictionary
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
for a in keys:
    sample_dict.pop(a)
print(sample_dict)

# Check if a value exists in a dictionary
sample_dict = {'a': 100, 'b': 300, 'c': 300}
if 200 in sample_dict.values():
    print("200 value is present")
else:
    print("200 is not present")

# Rename key of a dictionary
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

# Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(max(sample_dict,key=sample_dict.get))

# Change value of a key in a nested dictionary
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict["emp3"]["salary"]=8500
print(sample_dict)