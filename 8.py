import os
import shutil

FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx'],
    'Audio': ['.mp3', '.wav', '.aac'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.gz']
}

def organize_files(folder_path):
    for folder_name in FILE_TYPES.keys():
        folder_dir = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder_dir):
            os.makedirs(folder_dir)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            _ , file_extension = os.path.splitext(filename)
            moved = False
            for folder, extension in FILE_TYPES.items():
                if file_extension.lower() in extension:
                    destination = os.path.join(folder_path, folder,filename)
                    shutil.move(file_path,destination)
                    print(f'Moved {filename}-> {folder}')
                    moved = True
                    break
            if not moved:
                print(f'No matching folder for {filename}')

folder_to_organize = ''
organize_files(folder_to_organize)
    