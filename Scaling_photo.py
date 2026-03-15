import cv2 as cv

def fit_to_screen(image, max_width=900, max_height=700):
    height, width = image.shape[:2]
    scale = min(max_width / width, max_height / height, 1.0)
    new_size = (int(width * scale), int(height * scale))
    return cv.resize(image, new_size, interpolation=cv.INTER_AREA)

img = cv.imread('Photos/img.jpg')


if img is None:
    print("Image not found")

else:
    #normal image
    fitted_img = fit_to_screen(img)

    #gray image
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    fitted_gray = fit_to_screen(gray)

    #blurred image
    blurred = cv.GaussianBlur(img,(9,9),cv.BORDER_DEFAULT)
    fitted_blurred = fit_to_screen(blurred)

    cv.imshow('Normal pc', fitted_img)
    cv.imshow('Gray',fitted_gray)
    cv.imshow('Blurred',fitted_blurred)

    cv.waitKey(0)
    cv.destroyAllWindows()




