import json
import sys

notebook_path = sys.argv[1]

with open(notebook_path, 'r') as f:
    nb = json.load(f)

for cell in nb.get('cells', []):
    if 'id' in cell:
        del cell['id']

with open(notebook_path, 'w') as f:
    json.dump(nb, f, indent=1)