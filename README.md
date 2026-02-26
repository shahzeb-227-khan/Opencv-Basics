# OpenCV Basics

A beginner-friendly Python project that covers the fundamentals of **OpenCV (Open Source Computer Vision Library)** — reading, displaying, and resizing images and videos using Python.

---

## Table of Contents

- [About](#about)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Notes](#notes)

---

## About

This project demonstrates how to get started with OpenCV in Python. It covers two core concepts:

1. **Reading & displaying images** with custom rescaling.
2. **Capturing & displaying live video** from a webcam with frame resizing and resolution control.

---

## Project Structure

```
Opencv project/
│
├── Reading_photo.py       # Read and display a static image with rescaling
├── Reading_video.py       # Capture and display live webcam video with rescaling
│
├── Photos/                # Folder containing image assets
│   └── pc desk.jpg
│
└── Videos/                # Folder for video assets
```

---

## Prerequisites

- Python **3.x**
- A working **webcam** (required for `Reading_video.py`)

---

## Installation

1. **Clone or download** this repository to your local machine.

2. **Install OpenCV** via pip:

   ```bash
   pip install opencv-python
   ```

3. Place your images inside the `Photos/` folder and videos inside the `Videos/` folder.

---

## Usage

### Read & Display an Image

```bash
python Reading_photo.py
```

Opens two windows:
- `Pc` — the original image at full resolution.
- `Resized Pc` — the image rescaled to **75%** of its original size.

Press any key to close the windows.

---

### Capture & Display Live Video

```bash
python Reading_video.py
```

Opens two windows showing the live webcam feed:
- `Video` — the raw captured frame.
- `Resized Video` — the frame rescaled to **75%** of its original size.

Press **`d`** to stop the video capture and close the windows.

---

## Features

| Feature | Description |
|---|---|
| `rescaleFrame(frame, scale)` | Resizes any image or video frame by a given scale factor using `cv2.INTER_AREA` interpolation |
| `changeRes(width, height)` | Changes the resolution of a live video capture stream via `capture.set()` |
| Image Display | Displays both original and resized versions of an image side by side |
| Live Video Capture | Captures frames from webcam in real-time and displays rescaled output |

---

## Notes

- The default scale factor for `rescaleFrame` is **0.75** (75%). You can pass a custom value, e.g., `rescaleFrame(frame, scale=0.5)` for 50%.
- `changeRes()` only works with **live video captures** (`cv2.VideoCapture`), not static images or pre-recorded video files.
- Make sure the image path in `Reading_photo.py` matches the filename inside your `Photos/` folder.
