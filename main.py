from pathlib import Path
import shutil

downloads_path = Path(r'C:\Users\louka\Downloads')

# List files in Downloads directory

files = [p for p in Path(downloads_path).iterdir() if not p.is_dir()]

# Move files to different folders based on the file extension

for file in files:
    if file.suffix == '.doc' or file.suffix == '.docx':
        destination = 'C:/Users/louka/Documents'
        shutil.move(downloads_path / file.name, destination)
