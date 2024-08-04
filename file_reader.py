from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()

pi_string = ''
for content in contents.splitlines():
    pi_string += content.lstrip()

print(pi_string)
print(len(pi_string))