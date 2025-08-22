import os
import cv2
import numpy as np

class YoloLabeler:
    """Handles YOLO label creation and saving."""
    def __init__(self):
        self.class_id = 0
        self.selected_tree = None

    def update_class_id(self, text, root_folder):
        """Updates the class ID based on the selected tree."""
        if text and root_folder:
            self.selected_tree = text
            subfolders = [d for d in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, d))]
            self.class_id = subfolders.index(text) if text in subfolders else 0
            print(f"Selected tree: {text}, Class ID: {self.class_id}")

    def create_yolo_label(self, image, img_path, selected_tree):
        """Creates a YOLO label for a single image."""
        if image is None or not selected_tree:
            print("No image or tree selected.")
            return

        if image.shape[2] == 4:
            mask = image[:, :, 3]
        else:
            mask = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            print("No contours found.")
            return

        largest_contour = max(contours, key=cv2.contourArea)
        h, w = mask.shape
        normalized_points = largest_contour.reshape(-1, 2).astype(np.float32) / [w, h]
        points_str = ' '.join([f"{x:.6f} {y:.6f}" for x, y in normalized_points])
        yolo_label = f"{self.class_id} {points_str}"

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        base_name = os.path.splitext(os.path.basename(img_path))[0]
        txt_path = os.path.join(desktop_path, f"{base_name}.txt")

        with open(txt_path, 'w') as f:
            f.write(yolo_label + '\n')

        print(f"YOLO label saved to {txt_path}")

    def label_all_images(self, image_paths, selected_tree, root_folder, filter_settings):
        """Labels all images in the selected tree folder."""
        if not image_paths or not selected_tree:
            print("No images or tree selected.")
            return

        tree_folder = os.path.join(root_folder, selected_tree)
        if not os.path.exists(tree_folder):
            print(f"Folder {tree_folder} not found.")
            return

        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", selected_tree)
        if not os.path.exists(desktop_path):
            os.makedirs(desktop_path)
            print(f"New folder created: {desktop_path}")

        from image_processor import ImageProcessor
        processor = ImageProcessor()
        for img_path in [p for p in image_paths if selected_tree in os.path.basename(os.path.dirname(p))]:
            original, result = processor.apply_filters(img_path, filter_settings)
            if result is None:
                continue

            if result.shape[2] == 4:
                mask = result[:, :, 3]
            else:
                mask = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
                _, mask = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if not contours:
                print(f"No contours found for {img_path}")
                continue

            largest_contour = max(contours, key=cv2.contourArea)
            h, w = mask.shape
            normalized_points = largest_contour.reshape(-1, 2).astype(np.float32) / [w, h]
            points_str = ' '.join([f"{x:.6f} {y:.6f}" for x, y in normalized_points])
            yolo_label = f"{self.class_id} {points_str}"

            base_name = os.path.splitext(os.path.basename(img_path))[0]
            txt_path = os.path.join(desktop_path, f"{base_name}.txt")

            with open(txt_path, 'w') as f:
                f.write(yolo_label + '\n')

            print(f"YOLO label saved to {txt_path}")

        print(f"All images labeled for {selected_tree}.")