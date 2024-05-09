import json
a=b"\xe8\x8b\xb9\xe6\x9e\x9c"
k=a.decode('UTF-8')
print(k)
c = "hhh"
d = k.encode("UTF-8")
print(d)

dst = '苹果'.encode('utf-8')
print(dst)
print(dst.decode('utf-8'))
'''
json=json.loads(k)
code = json["code"]
print(k)
print(code)
if code=='400':
    print('ddd')'''