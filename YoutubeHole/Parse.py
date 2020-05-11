import sys
import re

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
        print(line)
        m = re.match(r"(.+) - YouTube\((.+)\)", line)
        if m is not None:
            data3.append((m.group(1), m.group(2)))
        else:
            print("COULD NOT MATCH\n\n\n")
    out = open(output_name, 'w', encoding='utf8')
    for t in data3:
        print(t[0], t[1], sep='\t')
        out.write(t[0]+'\t'+t[1]+'\n')
