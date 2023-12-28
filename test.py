my_json={"a":1,"b":2,"c":3,"d":4,"e":5}

print(my_json.keys())
print(type(my_json.keys()))
print(list(my_json.keys()))

print(my_json.values())
print(type(my_json.values()))
print(list(my_json.values()))

print(my_json.items())
print(type(my_json.items()))
print(list(my_json.items()))

x={name:age for name,age in enumerate(my_json.items())}
print(x)
x=dict(zip(my_json.keys(), my_json.values()))
print(x)