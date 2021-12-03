import sys
from pathlib import Path

file = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'

numbers = [
    int(line.strip())
    for line in Path(file).read_text().splitlines()
    if line.strip()
]
print("# numbers:", len(numbers))

pre = sys.maxsize
count = 0
for x in numbers:
    if pre < x:
        count += 1

    pre = x

print("increases:", count)
