import sys
import re
from collections import defaultdict

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: Parse.py [input] [output]")
        exit()

    input_name = sys.argv[1]
    output_name = sys.argv[2]
    inp = open(input_name, 'r', encoding='utf8')
    contents = inp.read()
    inp.close()
    data = contents.split(" |$| ")
    prev = ""
    data2 = []
    for entry in data:
        if prev != entry:
            data2.append(entry)
        prev = entry

    data3 = []
    for line in data2:
        m = re.match(r"(.+) - YouTube\((.+)\)", line)
        if m is not None:
            data3.append((m.group(1), m.group(2)))

    out = open(output_name, 'w', encoding='utf8')

    d = defaultdict()
    
    for t in data3:
        out.write(t[0]+'\t'+t[1]+'\n')
        for word in t[0].split():
            if len(word) > 2 and not word.isnumeric():
                word = word.lower()
                d.setdefault(word, 0)
                d[word] += 1

    items = list(d.items())
    items.sort(key=lambda x: x[1])
    print("Most common words:")
    for i in items[-10:]:
        print(i)
