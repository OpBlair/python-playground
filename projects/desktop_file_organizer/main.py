import os
import shutil

# Mapping of folder names to their respective extensions
file_extensions = {
    "videos": [".mp4", ".mkv", ".webm"],
    "music": [".mp3", ".wav"],
    "images": [".png", ".jpeg", ".jpg", ".gif"],
    "documents": [".pdf", ".doc", ".docx", ".md", ".pptx", ".xlsx", ".csv", ".txt"]
}

def organize_folder(target_path="."):
    # Check if the target directory exists
    if not os.path.exists(target_path):
        print(f"Error: The path '{target_path}' does not exist.")
        return

    # List all files and folders in the target directory
    items = os.listdir(target_path)
    
    print(f"Organizing files in: {os.path.abspath(target_path)}\n")

    for item in items:
        item_path = os.path.join(target_path, item)

        # Skip if it's a directory (we only want to sort files)
        if os.path.isdir(item_path):
            continue

        # Get the file extension and convert it to lowercase
        file_ext = os.path.splitext(item)[1].lower()

        # Find which category the file belongs to
        destination_folder = "others"  # Default fallback folder
        for category, extensions in file_extensions.items():
            if file_ext in extensions:
                destination_folder = category
                break

        # Build the full path for the destination folder
        dest_path = os.path.join(target_path, destination_folder)

        # Create the destination folder if it doesn't exist yet
        os.makedirs(dest_path, exist_ok=True)

        # Move the file into the category folder
        final_destination = os.path.join(dest_path, item)
        
        # Avoid errors if a file with the exact same name already exists in the folder
        if not os.path.exists(final_destination):
            shutil.move(item_path, final_destination)
            print(f"Moved: {item} -> {destination_folder}/")
        else:
            print(f"Skipped (already exists): {item}")

    print("\n" + "=" * 30)
    print("Folder organization complete!")
    print("=" * 30)

if __name__ == "__main__":
    target = input("Enter path to organize [default: current directory]: ").strip() or "."
    organize_folder(target)