import cv2 as cv
import numpy as np
import os as os

def get_requirements():
    print("\nOpenCV - Computer Vision Library (Install this version: opencv-contrib-python)\n")
    print("\nProgram Requirements:\n"
        + "1. Image Processing and Manipulation.\n"
        + "2. Import necessary libraries.\n"
        + "3. Research how to install any missing packages, if necessary.\n"
        + "4. Create at least three functions that are called by the program:\n"
        + "\ta. main(): calls at least two other functions.\n"
        + "\tb. get_requirements(): displays the program requirements\n"
        + "\tc. opencv(): displays the following data.\n"
        + "5. Use provided media files.\n"
        + "6.  When running program:\n"
        + "\ta. Document any issues.\n"
        + "\tb. Document solutions attempted.\n")
    print("***Research how to make it work using Jupyter Notebook***")

def opencv():
# read in images (return images as matrix of pixels)
# also, could draw an existing image
    img_cat = cv.imread('photos/cat.jpg')

    # image dimensions (in pixels)
    dimensions = img_cat.shape

    # image height, width, number of channels
    height = img_cat.shape[0]
    width = img_cat.shape[1]
    channels = img_cat.shape[2]

    print("\nMetadata (Note: Number of Channels (3) represent RGB channels.):")
    print("Dimensions: ", dimensions)
    print("Height: ", height)
    print("Width: ", width)
    print("Channels: ", channels)

    # imshow() takes 2 args: name of window to display and matrix of pixels to display
    # Note: image displayed in new window
    cv.imshow('Cat1', img_cat)
    # time in milliseconds for any key press (0 = infinite amount of time)
    cv.waitKey(0)

    # Next: read larger image
    img_cat_large = cv.imread('photos/cat_large.jpg')

    # Note: image will need to be resized/rescaled
    cv.imshow('Cat2', img_cat_large)

    # here, resized to 50% of original size
    resized_cat = rescaleFrame(img_cat_large)
    cv.imshow('Dog Resize', resized_cat)
    cv.waitKey(0)

    # read in videos
    # also, can use integer values for connected video source, e.g. VideoCapture(0)
    # create instance of VideoCapture class
    vid_dog = cv.VideoCapture('videos/dog.mp4')
    # video read frame-by-frame (using loop structure)
    # Note: very similar to reading file line-by-line w/read() function

    while True:
        isTrue, frame = vid_dog.read() # two args: reads frame, and if successful

        # Note: -215: Assertion failed error. Means no more frame available.
        # Same error if image path incorrect
        # Here, prevents -215: Assertion error for videos
        if type (frame) == type (None):
            break

        frame_resized = rescaleFrame(frame)

        cv.imshow('Dog', frame) # reads individual frame
        cv.imshow('Dog Resized', frame_resized)

        # stop video from playing indefinitely (prevent infinite loop)
        # if 20 milliseconds, and hex value of letter 'd' pressed, stop video
        if cv.waitKey(20) & 0xFF == ord('q'):
            break

    vid_dog.release() # release capture pointer
    cv.destroyAllWindows() # no more need for any windows

    # draw shapes and write text on images (sizes in pixels)
    # can draw 1) blank image, or 2) existing image
    # create blank image (uint8: 8-bit unsigned integer used for images)

    height = 480 # np rows
    width = 640 #np cols
    num_colors = 3 # np channels (B, G, R channels/colors)

    # np.zeros: Returns new array of given shape and type, filled with zeros.
    # a. display blank image
    blank_image = np.zeros((height, width, num_colors), dtype='uint8')
    cv.imshow('Blank', blank_image)

    # b. color image (BGR values)
    blank_image[:] = 255, 0, 0
    cv.imshow('Blue', blank_image)

    # c. color only range of pixels (red square in blue image)
    blank_image[100:200, 300:400] = 0, 0, 255
    cv.imshow('Blue w/ Red Square', blank_image)

    # d. draw rectangle (img, start_point, end_point, color, thickness)
    cv.rectangle(blank_image, (0, 0), (200, 200), (0, 255, 0), thickness = 2)
    cv.imshow('Rectangle', blank_image)

    # e. draw rectangle w/ filled color (same as thickness = -1)
    cv.rectangle(blank_image, (0, 0), (200, 200), (0, 255, 0), thickness = cv.FILLED)
    cv.imshow('Rectangle Filled', blank_image)

    # here, using ratio of height and width
    # Note: integer division operator // (only keeps whole numbers)
    cv.rectangle(blank_image, (0, 0), (blank_image.shape[1] // 4, blank_image.shape[0] // 4),
                    (255, 255, 255), thickness = -1)
    cv.imshow('Rectangle Filled Ratio', blank_image)

    # f. draw a circle (img, center, radius, color, thickness)
    cv.circle(blank_image, (blank_image.shape[1] // 2, blank_image.shape[0] // 2), 30,
                (0, 0, 0), thickness = 3)
    cv.imshow('Circle', blank_image)

    # g. draw line (img, start_point, end_point, color, thickness)
    cv.line(blank_image, (blank_image.shape[1], blank_image.shape[0]), (blank_image.shape[1] // 2, blank_image.shape[0] // 2),
                (255, 255, 255), thickness = 1)
    cv.imshow('Line', blank_image)

    # h. write text (img, text, origin, fontFace, fontScale, color, thickness)
    cv.putText(blank_image, 'Hello World!',
                (blank_image.shape[1] // 2, blank_image.shape[0] // 2), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 255, 0), thickness = 2)
    cv.imshow('Text', blank_image)
    cv.waitKey(0)

# resize/rescale images
# function accepts frame, and scale value (here, 50%)
def rescaleFrame(frame, scale=.50):
    # works for images, existing videos, and live video
    width = int(frame.shape[1] * scale) # convert float to integer
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

#     # resize frame to specific dimensions (resampling using pixel area relation)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
    
def changeRes(width, height):
    # *however*, only works for *live* video
    capture.set(3, width)
    capture.set(4, height)

def main():
    get_requirements()
    opencv()

if __name__ == "__main__":
    main()