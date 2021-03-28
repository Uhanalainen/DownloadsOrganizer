from pathlib import Path
import shutil

downloads_path = Path(r'C:\Users\louka\Downloads')

# List files in Downloads directory

files = [p for p in Path(downloads_path).iterdir() if not p.is_dir()]

compressed = ['.7z', '.zip']
docs = ['.doc', '.docx', '.pdf']
ebooks = ['.epub', '.mobi']
executables = ['.exe']
music = ['.flac', '.mp3']
pictures = ['.eps', '.gif', '.jpeg', '.jpg', '.png']
videos = ['.h264', '.mkv', '.mp4']

# Move files to different folders based on the file extension


def move_file(name, destination):
    shutil.move(downloads_path / name, destination)


for file in files:
    if file.suffix in compressed:
        destination = 'C:/Users/louka/Zip'
    elif file.suffix in docs:
        if file.suffix == '.pdf':
            destination = 'C:/Users/louka/Documents/PDF'
        else:
            destination = 'C:/Users/louka/Documents/Doc'
    elif file.suffix in ebooks:
        destination = 'C:/Users/louka/Documents/ebook'
    elif file.suffix in executables:
        destination = 'C:/Users/louka/Exe'
    elif file.suffix in music:
        destination = 'C:/Users/louka/Music'
    elif file.suffix in pictures:
        destination = 'C:/Users/louka/Pictures'
    elif file.suffix in videos:
        destination = 'C:/Users/louka/Videos'
    else:
        destination = 'C:/Users/louka/Documents'
    move_file(file.name, destination)
