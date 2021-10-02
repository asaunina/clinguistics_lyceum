import re
import json

def words(stringIterable):
    lineStream = iter(stringIterable)
    for line in lineStream:
        for word in line.split():
            yield word
            
text = []          
with open('my.txt', 'r', newline = '') as file:
    for word in words(file):
        text.append(word)
    regex_num = re.compile('.-\d+')
    s = regex_num.findall(str(text))
    res = list(set(s))
    res.remove('3-4')
print(res)

for i in range (0, len(res)):
    names = res[i].split('-')
    print(json.dumps({'name (letter)' : names[0], 'name (number)' : names[1] }, ensure_ascii = False))
