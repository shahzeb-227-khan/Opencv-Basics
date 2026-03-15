import cv2 as cv
from pathlib import Path

img_path = Path(__file__).parent / "Photos" / "pc desk.jpg"
img = cv.imread(str(img_path))

if img is None:
    raise FileNotFoundError(f"Could not load image: {img_path}")

def fit_to_screen(image, max_width=900, max_height=700):
    height, width = image.shape[:2]
    scale = min(max_width / width, max_height / height, 1.0)
    new_size = (int(width * scale), int(height * scale))
    return cv.resize(image, new_size, interpolation=cv.INTER_AREA)


small_img = fit_to_screen(img)
cv.imshow("Pc", small_img)
cv.waitKey(0)
cv.destroyAllWindows()