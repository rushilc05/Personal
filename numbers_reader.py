from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
numebrs = json.loads(contents)

print(numebrs)