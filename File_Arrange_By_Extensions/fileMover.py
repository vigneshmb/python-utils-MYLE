import os
import shutil

def getFileCount():
        length = len(os.listdir(os.getcwd()))
        return length

def moveFiles():
    source_folder = os.getcwd();
    destination_folders = {
        "Compressed": [".zip", ".rar", ".7z",".tar"],
        "Documents": [".pdf", ".docx", ".txt",".xls",".xlsx",".csv",".doc"],
        "Coding Files":[".html",".css",".js",".jsx",".ts",".sql",".json",".har",".xml"],
        "Music": [".mp3", ".aac", ".wav"],
        "Videos": [".mp4", ".mov", ".avi",".mkv",".flv"],
        "Images": [".jpg",".jpeg", ".png", ".gif",".webp"],
        "Programs": [".exe", ".msi",".iso"],
    }

    count = 0

    for file in os.listdir(source_folder):
        file_path = os.path.join(source_folder, file)
        if os.path.isfile(file_path):
            for folder, extensions in destination_folders.items():
                if any(file.endswith(ext) for ext in extensions):
                    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)
                    shutil.move(file_path, os.path.join(source_folder, folder))
                    count+=1
    return count


if __name__ == "__main__":
    currFolder = os.getcwd()
    fileCount = getFileCount()
    print(f"Current folder - ({currFolder}) has {fileCount} files")
    moveCount = moveFiles()
    print(f"{moveCount} files out of {fileCount} are moved.\nRemaining files doesn't matches any given creteria")