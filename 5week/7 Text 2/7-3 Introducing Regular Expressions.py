source = open("D:\pg1342.txt")
pride = source.read()
print(pride[:1000])
import re
result = re.findall('[AEIOUaeiou]', pride)
print(len(result))
print(result)
print(result[:20])
# quotes = re.findall('"[^"]*\r\n\r\n|"[^"]*"', pride)
# print(len(quotes))
# print(quotes[:10])

pride_words = pride.split()
print(len(pride_words))
pride_words_2 = re.findall('[A-Za-z]', pride)
print(pride_words_2)
print(len(pride_words_2))
print(pride_words_2[4000:4050])
