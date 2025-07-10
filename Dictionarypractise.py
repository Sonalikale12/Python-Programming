# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(thisdict)

# The dict() Constructor
# thisdict = dict(name = "John", age = 36, country = "Norway")
# print(thisdict)

# D1={"Name":"Sonali","number":11,"Flatno":908,"name":"Sharvi"}
# x=D1.values()
# print(x)

# Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# dict3 = {**dict1,**dict2}
# # dict3=dict1.copy()
# # dict3.update(dict2)
# print(dict3)

# Initialize dictionary with default values
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
# dict1= dict.fromkeys(employees,defaults)
# print(dict1)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model","year")
print(thisdict)
