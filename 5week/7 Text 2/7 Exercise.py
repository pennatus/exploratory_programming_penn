source = open("D:\hitmanforum.txt")
hitman = source.read()
import re
result = re.findall('\dd|\dm', hitman)
print(result)
print(len(result))
