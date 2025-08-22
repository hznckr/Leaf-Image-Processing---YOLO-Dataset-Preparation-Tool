from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QCheckBox, QComboBox
from PyQt5.QtCore import Qt

class UIComponents:
    """Handles creation and setup of UI components."""
    def __init__(self):
        self.original_label = QLabel("Original Image")
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        
        self.result_label_widget = QLabel("Filtered Image")
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)
        
        self.hsv_checkbox = QCheckBox("HSV Filter")
        self.canny_checkbox = QCheckBox("Canny Edge")
        self.kmeans_checkbox = QCheckBox("K-Means Segmentation")
        self.threshold_checkbox = QCheckBox("Threshold")
        self.crop_checkbox = QCheckBox("Crop")
        self.transparent_checkbox = QCheckBox("Transparent Background")
        
        self.open_button = QPushButton("Select Folder")
        self.prev_button = QPushButton("← Previous")
        self.next_button = QPushButton("Next →")
        self.apply_button = QPushButton("Apply Filter")
        self.label_button = QPushButton("Label All")
        
        self.tree_combo = QComboBox()

    def setup_layout(self):
        """Sets up the layout for UI components."""
        hbox = QHBoxLayout()
        hbox.addWidget(self.hsv_checkbox)
        hbox.addWidget(self.canny_checkbox)
        hbox.addWidget(self.kmeans_checkbox)
        hbox.addWidget(self.threshold_checkbox)
        hbox.addWidget(self.crop_checkbox)
        hbox.addWidget(self.transparent_checkbox)

        button_box = QHBoxLayout()
        button_box.addWidget(self.open_button)
        button_box.addWidget(self.prev_button)
        button_box.addWidget(self.next_button)
        button_box.addWidget(self.apply_button)
        button_box.addWidget(self.label_button)
        button_box.addWidget(QLabel("Select Tree:"))
        button_box.addWidget(self.tree_combo)

        img_box = QHBoxLayout()
        original_vbox = QVBoxLayout()
        original_vbox.addWidget(self.original_label)
        original_vbox.addWidget(self.image_label)
        result_vbox = QVBoxLayout()
        result_vbox.addWidget(self.result_label_widget)
        result_vbox.addWidget(self.result_label)
        img_box.addLayout(original_vbox)
        img_box.addLayout(result_vbox)

        main_vbox = QVBoxLayout()
        main_vbox.addLayout(img_box)
        main_vbox.addLayout(hbox)
        main_vbox.addLayout(button_box)
        return main_vbox