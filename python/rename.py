import os
import shutil

def rename_images(folder_path):
    # Get a list of all files in the folder directory
    files = os.listdir(folder_path)

    # Filter only image files (you can modify this condition as needed)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = [file for file in files if any(file.lower().endswith(ext) for ext in image_extensions)]

    # Sort the image files alphabetically
    image_files.sort()

    # Rename and move the files sequentially
    for index, old_name in enumerate(image_files):
        extension = os.path.splitext(old_name)[1]
        new_name = f"Lauren_{index + 1}{extension}"
        old_path = os.path.join(folder_path, old_name)
        new_path = os.path.join(folder_path, new_name)
        shutil.move(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

if __name__ == "__main__":
    folder_path = "C:\\Users\\lecoo\\OneDrive\\Desktop\\python"
    rename_images(folder_path)
