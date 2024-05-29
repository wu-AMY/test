import json

d = {
    "name": "zhangsan",
    "age": 12
}

j = json.dumps(d)
json.dump()
k = json.loads(j)

print(j)