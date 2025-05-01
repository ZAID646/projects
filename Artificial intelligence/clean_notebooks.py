import nbformat
import os

def clean_widgets_metadata(file_path):
    try:
        nb = nbformat.read(file_path, as_version=nbformat.NO_CONVERT)
        if 'widgets' in nb.metadata:
            print(f"Cleaning widgets in: {file_path}")
            del nb.metadata['widgets']
            nbformat.write(nb, file_path)
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".ipynb"):
            full_path = os.path.join(root, file)
            clean_widgets_metadata(full_path)
