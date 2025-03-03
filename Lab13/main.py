import re

text = " 555-1234 "

pattern = r"\d{3}-\d{4}"

pn = re.findall(pattern, text)
print(pn)

text2 = "Hello,fadsfsaf"
text3 = "Greetings! Hello dsadsada"

pattern2 = r"Hello"

match1 = re.match(pattern2, text2)
if match1:
    print(True, match1.group())

match2 = re.match(pattern2, text3)
if match2:
    print(True, match2.group())
else:
    print(False)
search = re.search(pattern2, text2)
if search:
    print(True, search.group())

text4 = "There are 3, 4 ,5 and 6"

pattern3 = r"\d+"

res = re.sub(pattern3, "NUMBER", text4)
print(res)

text_email = "contact = support@email.com or abrakadabra@mail.ru"
pattern_email = r"\b\w+@\w+\.\w+\b"

res = re.findall(pattern_email, text_email)
print(res)

text_vowels = "An apple a day keeps the doctor away. Even elephants enjoy eating"
text_vowels = text_vowels.lower()
pattern_vowels = r"\b[aeiou]\w*\b"

res = re.findall(pattern_vowels, text_vowels)

print(res)

