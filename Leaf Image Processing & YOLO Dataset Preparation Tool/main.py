import sys
from PyQt5.QtWidgets import QApplication
from image_filter_app import ImageFilterApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageFilterApp()
    window.show()
    sys.exit(app.exec_())