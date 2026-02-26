import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

#Works on live video 
def changeRes(width,height):
    capture.set(3,width)
    capture.set(4,height)


capture = cv.VideoCapture(0)

while True:
    isTrue,frame = capture.read()
    resoluted_frame = rescaleFrame(frame)
    cv.imshow('Video',resoluted_frame)

    resized_frame = rescaleFrame(frame)
    cv.imshow('Resized Video',resized_frame)

    if cv.waitKey(20) & 0xff == ord('d'):
        break


capture.releas()
cv.destroyAllWindows()