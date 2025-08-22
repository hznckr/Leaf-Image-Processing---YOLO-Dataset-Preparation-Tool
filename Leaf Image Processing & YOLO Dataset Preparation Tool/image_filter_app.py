import os
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from ui_components import UIComponents
from image_loader import ImageLoader
from image_processor import ImageProcessor
from yolo_labeler import YoloLabeler

class ImageFilterApp(QWidget):
    """Main application class for the image filter GUI."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Processing Interface")
        self.ui = UIComponents()
        self.loader = ImageLoader()
        self.processor = ImageProcessor()
        self.labeler = YoloLabeler()
        self.init_ui()

    def init_ui(self):
        """Initializes the UI and connects signals."""
        self.setLayout(self.ui.setup_layout())
        
        self.ui.open_button.clicked.connect(self.open_folder)
        self.ui.prev_button.clicked.connect(self.prev_image)
        self.ui.next_button.clicked.connect(self.next_image)
        self.ui.apply_button.clicked.connect(self.apply_filters)
        self.ui.label_button.clicked.connect(self.label_all_images)
        self.ui.tree_combo.currentTextChanged.connect(self.update_class_id)

    def update_class_id(self, text):
        """Updates the class ID when the tree selection changes."""
        self.labeler.update_class_id(text, self.loader.root_folder)

    def open_folder(self):
        """Handles folder selection and populates the tree combo."""
        subfolders = self.loader.open_folder(self)
        self.ui.tree_combo.clear()
        for subfolder in sorted(subfolders):
            self.ui.tree_combo.addItem(subfolder, subfolder)
        if self.loader.image_paths:
            current_folder = os.path.basename(os.path.dirname(self.loader.image_paths[self.loader.current_index]))
            if subfolders and current_folder in subfolders:
                self.ui.tree_combo.setCurrentText(current_folder)
                self.labeler.update_class_id(current_folder, self.loader.root_folder)
            self.show_image()

    def show_image(self):
        """Displays the current image."""
        img_path = self.loader.get_current_image_path()
        if img_path:
            pixmap = QPixmap(img_path)
            self.ui.image_label.setPixmap(pixmap.scaled(300, 300, Qt.KeepAspectRatio))
            current_folder = os.path.basename(os.path.dirname(img_path))
            if self.ui.tree_combo.count() > 0:
                self.ui.tree_combo.setCurrentText(current_folder)
                self.labeler.update_class_id(current_folder, self.loader.root_folder)

    def prev_image(self):
        """Navigates to the previous image and displays it."""
        img_path = self.loader.prev_image()
        if img_path:
            self.show_image()

    def next_image(self):
        """Navigates to the next image and displays it."""
        img_path = self.loader.next_image()
        if img_path:
            self.show_image()

    def apply_filters(self):
        """Applies filters to the current image and displays the result."""
        filter_settings = {
            'hsv': self.ui.hsv_checkbox.isChecked(),
            'canny': self.ui.canny_checkbox.isChecked(),
            'kmeans': self.ui.kmeans_checkbox.isChecked(),
            'threshold': self.ui.threshold_checkbox.isChecked(),
            'crop': self.ui.crop_checkbox.isChecked(),
            'transparent': self.ui.transparent_checkbox.isChecked()
        }
        original, result = self.processor.apply_filters(self.loader.get_current_image_path(), filter_settings)
        if original is not None:
            qimg_original = self.processor.convert_to_qimage(original)
            self.ui.image_label.setPixmap(QPixmap.fromImage(qimg_original).scaled(300, 300, Qt.KeepAspectRatio))
        if result is not None:
            qimg_result = self.processor.convert_to_qimage(result)
            self.ui.result_label.setPixmap(QPixmap.fromImage(qimg_result).scaled(300, 300, Qt.KeepAspectRatio))
            self.labeler.create_yolo_label(result, self.loader.get_current_image_path(), self.labeler.selected_tree)

    def label_all_images(self):
        """Labels all images in the selected tree folder."""
        filter_settings = {
            'hsv': self.ui.hsv_checkbox.isChecked(),
            'canny': self.ui.canny_checkbox.isChecked(),
            'kmeans': self.ui.kmeans_checkbox.isChecked(),
            'threshold': self.ui.threshold_checkbox.isChecked(),
            'crop': self.ui.crop_checkbox.isChecked(),
            'transparent': self.ui.transparent_checkbox.isChecked()
        }
        self.labeler.label_all_images(self.loader.image_paths, self.labeler.selected_tree, self.loader.root_folder, filter_settings)