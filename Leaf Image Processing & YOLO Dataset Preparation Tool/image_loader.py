import os
from PyQt5.QtWidgets import QFileDialog

class ImageLoader:
    """Manages loading and navigating images from a folder."""
    def __init__(self):
        self.image_paths = []
        self.current_index = 0
        self.root_folder = None

    def open_folder(self, parent_widget):
        """Opens a folder and loads image paths."""
        folder = QFileDialog.getExistingDirectory(parent_widget, "Select Folder")
        if folder:
            print(f"Selected folder: {folder}")
            self.root_folder = os.path.dirname(folder) if os.path.basename(folder) in [d for d in os.listdir(os.path.dirname(folder)) if os.path.isdir(os.path.join(os.path.dirname(folder), d))] else folder
            print(f"Root folder: {self.root_folder}")
            self.image_paths = []

            for file in os.listdir(folder):
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    self.image_paths.append(os.path.join(folder, file))

            subfolders = [d for d in os.listdir(self.root_folder) if os.path.isdir(os.path.join(self.root_folder, d))]
            print(f"Detected subfolders: {subfolders}")
            for subfolder in sorted(subfolders):
                subfolder_path = os.path.join(self.root_folder, subfolder)
                for file in os.listdir(subfolder_path):
                    if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                        self.image_paths.append(os.path.join(subfolder_path, file))

            self.image_paths.sort()
            if self.image_paths:
                self.current_index = 0
            else:
                print("No images found in the selected folder.")
            return subfolders
        else:
            print("Folder selection canceled.")
            return []

    def get_current_image_path(self):
        """Returns the path of the current image."""
        return self.image_paths[self.current_index] if self.image_paths else None

    def prev_image(self):
        """Navigates to the previous image."""
        if self.image_paths:
            self.current_index = (self.current_index - 1) % len(self.image_paths)
            return self.get_current_image_path()
        return None

    def next_image(self):
        """Navigates to the next image."""
        if self.image_paths:
            self.current_index = (self.current_index + 1) % len(self.image_paths)
            return self.get_current_image_path()
        return None