'''
JSON stands for JavaScript Object Notation
JSON is a lightweight format for storing and transporting data
JSON is often used when data is sent from a server to a web page
JSON is "self-describing" and easy to understand
'''
#Convert from JSON to Python:
import json

# some JSON:
x = '{ "name":"Toshi", "age":30, "city":"Pune"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])         # output : 30
print(y["name"])        # output : Toshi
print(y["city"])        # output : Pune
print(y)                # output : {'name': 'Toshi', 'age': 30, 'city': 'Pune'}


#Convert from Python to JSON:
# a Python object (dict):
x = {
  "name": "Toshi",
  "age": 30,
  "city": "Pune"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)            #{"name": "Toshi", "age": 30, "city": "Pune"}


#Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

'''
output:
{"name": "John", "age": 30}
["apple", "bananas"]
["apple", "bananas"]
"hello"
42
31.76
true
false
null
'''
