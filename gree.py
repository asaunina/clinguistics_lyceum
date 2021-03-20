import csv
import re
from fuzzywuzzy import fuzz

with open('greedy.csv', newline='', encoding='utf8') as File:
    reader = csv.reader(File)
    included_cols = [1]
    for row in reader:
        content = list(row[i] for i in included_cols)
        for line in content:
            result = re.findall(r'(соленый огурец|солёный огурец|Соленый огурец|Солёный огурец)', line)
            if len(result)>0:
                res = fuzz.ratio(line, 'Соленый огурец на полу валяется, никто его не ест')
                print(res, line)
                

            
