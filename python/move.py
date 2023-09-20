import os
import shutil
import math

def distribute_images(source_folder, num_folders):
    # Get a list of all files in the source folder
    files = os.listdir(source_folder)

    # Filter only image files (you can modify this condition as needed)
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_files = [file for file in files if any(file.lower().endswith(ext) for ext in image_extensions)]

    # Ensure there are enough images to distribute
    total_images = len(image_files)
    images_per_folder = int(math.ceil(total_images / num_folders))

    if total_images < num_folders:
        print("Not enough images to distribute.")
        return

    # Create destination folders if they don't exist
    for folder_num in range(1, num_folders + 1):
        folder_name = f"destination_folder_{folder_num}"
        folder_path = os.path.join(source_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)

    # Distribute images to destination folders
    for folder_num in range(1, num_folders + 1):
        folder_name = f"destination_folder_{folder_num}"
        folder_path = os.path.join(source_folder, folder_name)

        for _ in range(images_per_folder):
            if not image_files:
                break

            image_name = image_files.pop(0)
            source_path = os.path.join(source_folder, image_name)
            destination_path = os.path.join(folder_path, image_name)
            shutil.move(source_path, destination_path)
            print(f"Moved {image_name} to {folder_name}")

if __name__ == "__main__":
    source_folder = "C:\\Users\\lecoo\\OneDrive\\Desktop\\python"
    num_folders = 5

    distribute_images(source_folder, num_folders)
