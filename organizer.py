import os
import shutil

def organize_files(directory):
    # Mapping of file extensions to folder names
    extension_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx', '.csv'],
        'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
        'Audio': ['.mp3', '.wav', '.flac'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.sh', '.bat']
    }

    if not os.path.exists(directory):
        print(f'Error: Directory {directory} does not exist.')
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Skip directories
        if os.path.isdir(filepath):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for folder, extensions in extension_map.items():
            if file_ext in extensions:
                dest_folder = os.path.join(directory, folder)
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(filepath, os.path.join(dest_folder, filename))
                print(f'Moved: {filename} -> {folder}/')
                moved = True
                break
        
        if not moved and file_ext:
            other_folder = os.path.join(directory, 'Others')
            os.makedirs(other_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(other_folder, filename))
            print(f'Moved: {filename} -> Others/')

if __name__ == '__main__':
    # Organize current directory by default
    organize_files('.')