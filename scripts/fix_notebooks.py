import json
import os

for root, dirs, files in os.walk('notebooks'):
    for file in files:
        if file.endswith('.ipynb'):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                nb = json.load(f)
            for cell in nb.get('cells', []):
                if 'id' in cell:
                    del cell['id']
            with open(path, 'w') as f:
                json.dump(nb, f, indent=1)