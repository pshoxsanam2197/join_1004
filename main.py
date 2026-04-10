# 1-m
words = ["Hello", "world"]
result = " ".join(words)

print(result)

# 2-m
items = ["apple", "banana", "cherry"]
result = ", ".join(items)

print(result)

# 3-m
chars = ["P", "Y", "T", "H", "O", "N"]
result = "".join(chars)

print(result)

# 4-m
numbers = [1, 2, 3, 4]

result = ", ".join(map(str, numbers))
print(result)

# 5-m
words = ["I", "love", "Python"]

# noto‘g‘ri usul (sekin)
result = ""
for word in words:
    result += word + " "

print(result)

# to‘g‘ri usul (tez)
result = " ".join(words)
print(result)

# 6-m
folders = ["home", "user", "documents"]
path = "/".join(folders)

print(path)

# 7-m
words = ["Python", "", "Django", None, "API"]

result = " ".join([w for w in words if w])
print(result)

# 8-m
word = "Python"

result = "-".join(word)
print(result)

# 9-m
words = ["python", "backend", "api"]

result = " | ".join([w.upper() for w in words])
print(result)

# 10-m
data = {"name": "Ali", "age": 20}

result = ", ".join(data.keys())
print(result)

# 11-m
params = {"page": 1, "limit": 10}

query = "&".join([f"{k}={v}" for k, v in params.items()])
url = f"/api?{query}"

print(url)

# 12-m
row = ["Ali", "20", "Tashkent"]

csv_line = ",".join(row)
print(csv_line)

# 5-m
s = 'hello'
result = "*".join(s)
print(result)

# 6-m
s = ["line1", "line2", "line3"]
result = "\n".join(s)
print(result)

# 7-m
d = ["backend", "frontend", "devops"]
result = '|'.join(d)
print(result)

# 8-m
list = []
print(''.join(list))

# 10-m
matn = ["I", "Love", "AI"]
res = ''.join(matn)
print(res)

# 11-m
nums = [1, 2, 3, 4, 5]
result = ", ".join(map(str, nums))
print(result)

# 12-m
lst = ["Python", "", "Django", "", "API"]
result = " ".join(filter(None, lst))
print(result)

# 13-m
lst = ["python", "backend", "api"]
result = "_".join(word.upper() for word in lst)
print(result)

# 14-m
d = {"name": "Ali", "age": 20, "city": "Tashkent"}
result = ", ".join(d.keys())
print(result)

# 15-m
lst = ["python", "django", "api"]
result = " ".join(f"#{word}" for word in lst)
print(result)

# 16-m
lst = ["python", "django", "api"]
result = " ".join(f"#{word}" for word in lst)
print(result)

# 17-m
lst = ["abc", "def", "ghi"]
result = " ".join(s[::-1] for s in lst)
print(result)

# 18-m
lst = ["hi", "python", "js", "django"]
result = " ".join(word for word in lst if len(word) > 3)
print(result)

# 19-m
s = "CODE"
result = ".".join(s)
print(result)

# 20-m
lst = ["home", "user", "downloads", "file.txt"]
result = "/".join(lst)
print(result)
