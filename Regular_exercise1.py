import re

# Practise all regular expressions functions
txt = "It is amazing today"

c = re.search("^It.*today$", txt)
if c:
    print("Found")
else:
    print("No match")

x = re.findall("am", txt)
print(x)

y = re.search("\s", txt)
print('The first white-space character is located in position:', y.start())

d= re.search("nice", txt)
print(d)

q = re.split("\s", txt)
print(q)

p = re.split("\s", txt, 1)
print(p)

m = re.sub("\s", "8", txt)
print(m)

n = re.sub("\s", "8", txt, 2)
print(n)

k = re.search("i", txt)
print(k)

u = re.search(r"\ba\w+", txt)
print(u.span())

a = re.search(r"\ba\w+", txt)
print(a.string)

b = re.search(r"\ba\w+", txt)
print(b.group())