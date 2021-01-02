
textfile = open('abc.text')

lines = textfile.readlines()

for line in reversed(lines):
    print(line)

textfile.close()