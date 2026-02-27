"""
draw.py
-------
Demonstrates basic OpenCV drawing functions on a blank NumPy canvas.

Topics covered:
    1. Creating a blank canvas
    2. Painting the canvas a solid colour
    3. Drawing a rectangle
    4. Drawing a circle
    5. Drawing a line
    6. Writing text

Author : Shahzeb
"""

import cv2 as cv
import numpy as np


# ---------------------------------------------------------------------------
# Canvas setup
# ---------------------------------------------------------------------------
HEIGHT, WIDTH = 500, 500
blank = np.zeros((HEIGHT, WIDTH, 3), dtype='uint8')


def show(title: str, img) -> None:
    """Display an image window with the given title."""
    cv.imshow(title, img)


# ---------------------------------------------------------------------------
# 1. Blank canvas
# ---------------------------------------------------------------------------
show('1 - Blank Canvas', blank.copy())

# ---------------------------------------------------------------------------
# 2. Paint the canvas a solid colour (green)
# ---------------------------------------------------------------------------
green_canvas = blank.copy()
green_canvas[:] = (0, 255, 0)               # BGR: green
show('2 - Solid Colour (Green)', green_canvas)

# ---------------------------------------------------------------------------
# 3. Draw a rectangle
#    cv.rectangle(img, top-left, bottom-right, colour_BGR, thickness)
#    thickness=-1 fills the shape
# ---------------------------------------------------------------------------
rect_canvas = blank.copy()
cv.rectangle(rect_canvas, (0, 0), (WIDTH // 2, HEIGHT), (0, 0, 255), thickness=2)
show('3 - Rectangle', rect_canvas)

# ---------------------------------------------------------------------------
# 4. Draw a circle
#    cv.circle(img, centre, radius, colour_BGR, thickness)
# ---------------------------------------------------------------------------
circle_canvas = blank.copy()
centre = (WIDTH // 2, HEIGHT // 2)
cv.circle(circle_canvas, centre, 40, (255, 0, 0), thickness=3)
show('4 - Circle', circle_canvas)

# ---------------------------------------------------------------------------
# 5. Draw a line
#    cv.line(img, start_point, end_point, colour_BGR, thickness)
# ---------------------------------------------------------------------------
line_canvas = blank.copy()
cv.line(line_canvas, (0, 0), (WIDTH // 2, HEIGHT // 2), (255, 255, 255), thickness=3)
show('5 - Line', line_canvas)

# ---------------------------------------------------------------------------
# 6. Write text
#    cv.putText(img, text, org, font, font_scale, colour_BGR, thickness)
# ---------------------------------------------------------------------------
text_canvas = blank.copy()
cv.putText(
    text_canvas,
    'Learn OpenCV with Shahzeb',
    (0, HEIGHT // 2),
    cv.FONT_HERSHEY_TRIPLEX,
    1.0,
    (0, 255, 255),
    thickness=2,
)
show('6 - Text', text_canvas)

# ---------------------------------------------------------------------------
# Wait for any key press, then close all windows
# ---------------------------------------------------------------------------
cv.waitKey(0)
cv.destroyAllWindows()