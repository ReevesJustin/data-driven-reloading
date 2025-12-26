import json
import base64
import os

# Load the executed notebook
with open('notebooks/executed/01_The_Biggest_Lie_in_Reloading_Testing.ipynb', 'r') as f:
    notebook = json.load(f)

# Directory to save images
output_dir = 'notebooks/static/'
os.makedirs(output_dir, exist_ok=True)

# Counter for image files
image_count = 0

# Iterate through cells
for cell in notebook['cells']:
    if cell['cell_type'] == 'code' and 'outputs' in cell:
        for output in cell['outputs']:
            if 'data' in output and 'image/png' in output['data']:
                # Decode and save the image
                image_data = output['data']['image/png']
                image_bytes = base64.b64decode(image_data)
                image_filename = f'{output_dir}plot_{image_count + 1}.png'
                with open(image_filename, 'wb') as img_file:
                    img_file.write(image_bytes)
                print(f'Saved {image_filename}')
                image_count += 1

print(f'Extracted {image_count} images.')