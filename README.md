# Leaf Image Processing & YOLO Dataset Preparation Tool
Leaf image processing and YOLO dataset preparation with an intuitive GUI.

---

## Description
A PyQt5-based desktop application for leaf image processing, applying filters, segmentation, and generating YOLO annotation files.  
This tool simplifies dataset preparation for YOLO models by offering batch filtering, automatic labeling, and a user-friendly GUI.

---

## Features
- Apply multiple image filters: HSV, Canny, K-Means, Threshold, Crop, Transparent Background
- Batch process images
- Automatic YOLO annotation generation
- Class selection based on folder structure
- User-friendly GUI

---

## Dataset
The Flavia dataset contains 1,907 leaf images from 32 plant species, each with 50–77 images.  
It is widely used for leaf classification tasks.

You can download the dataset from the official SourceForge page:  
[Download Flavia Leaf Dataset](https://sourceforge.net/projects/flavia/files/Leaf%20Image%20Dataset/1.0/Leaves.tar.bz2/download)

After downloading, extract the dataset and organize the images into folders by species.  
Each folder should be named according to the plant species (e.g., `Acer_Palmatum`, `Berberis_Anhweiensis`).  
This structure will facilitate the automatic class labeling feature of the tool.

For more information and resources, visit the official Flavia project page:  
[Flavia Project on SourceForge](https://flavia.sourceforge.net/)

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Git
- pip (Python package manager)

### Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/hznckr/leaf-yolo-tool.git
2.Navigate to the project directory

    cd leaf-yolo-tool
3.Install dependencies
   Option 1: Using requirements.txt (recommended)

    pip install -r requirements.txt
  
   Option 2: Install manually
   
     pip install PyQt5 opencv-python numpy

4.Run the application

     python main.py
    
