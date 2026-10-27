# Image Processing Lab Assignments

## Program 1: Read and Display an Image Using OpenCV

**Objective:** Read `flower.jpg` with OpenCV, print its dimensions and data type, and display it with the title **Original Image**.

### Files
- `Program_01_Read_Display_Image.py` — Program 1 source code
- `flower.jpg` — sample image used by Program 1
- `requirements.txt` — required Python packages

### Install dependencies
```bash
python -m pip install -r requirements.txt
```

### Run
Run from this folder:
```bash
python Program_01_Read_Display_Image.py
```

Keep `flower.jpg` in the same folder as the Python script. The script reports a clear error if the image is missing or unreadable.

**Note:** OpenCV reads colour images in BGR order. The program converts BGR to RGB before displaying the image with Matplotlib.
