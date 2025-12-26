import json
import os
import glob

# Directory with notebooks
notebook_dir = 'notebooks'
md_dir = 'notebooks/md'

# Find all .ipynb files
notebooks = glob.glob(os.path.join(notebook_dir, '*.ipynb'))

for nb_path in notebooks:
    with open(nb_path, 'r') as f:
        notebook = json.load(f)
    
    # Extract markdown cells
    md_content = []
    for cell in notebook['cells']:
        if cell['cell_type'] == 'markdown':
            source = ''.join(cell['source'])
            md_content.append(source)
    
    # Join with double newlines
    full_md = '\n\n'.join(md_content)
    
    # Output filename
    base_name = os.path.basename(nb_path).replace('.ipynb', '.md')
    md_path = os.path.join(md_dir, base_name)
    
    with open(md_path, 'w') as f:
        f.write(full_md)
    
    print(f'Converted {nb_path} to {md_path}')

print('All notebooks converted to markdown.')