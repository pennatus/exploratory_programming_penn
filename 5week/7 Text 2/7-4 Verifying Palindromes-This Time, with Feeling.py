import re
test = 'Here is a nice string. La la la.'
print(re.sub('\W+', '', test))

def pal(text):
    return text.lower() == text[::-1].lower()

def prep(text):
    return re.sub('\W+', '', text)

palindrome = 'Star comedy by Democrats'
print(pal(prep(palindrome)))
otherwise = "This is almost a palindrome ... er, actually it's not."
print(pal(prep(otherwise)))
