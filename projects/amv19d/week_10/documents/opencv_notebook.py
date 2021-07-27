import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline

def opencv():
    img_dog = cv.imread('photos/dog.jpg')

    dimensions = img_dog.shape

    height = img_dog.shape[0]
    width = img_dog.shape[1]
    channels = img_dog.shape[2]

    print("\nMetadata (Note: Number of Channels (3) represent RGB channels.):")
    print("Dimensions: ", dimensions)
    print("Height: ", height)
    print("Width: ", width)
    print("Channels: ", channels)

    print('\nLOOK AT ALL OF THIS WASTED SPACE!!')

    plt.title('Dog - BGR', fontweight = "bold")
    plt.imshow(img_dog)
    plt.show()

    plt.title('Dog - BGR', fontweight = "bold")
    plt.imshow(cv.cvtColor(img_dog, cv.COLOR_BGR2RGB))
    plt.show()


    img1 = cv.imread('photos/dog.jpg')
    img2 = cv.imread('photos/dog.jpg')

    NUM_ROWS = 1
    IMGs_IN_ROW = 2
    f, ax = plt.subplots(NUM_ROWS, IMGs_IN_ROW, figsize=(16,6))

    ax[0].imshow(img1)
    # ax[1].imshow(img2)
    ax[1].imshow(cv.cvtColor(img2, cv.COLOR_BGR2RGB))

    ax[0].set_title('Blue Dog')
    ax[1].set_title('Happy Dog -- or, maybe not!')

    title = ('Side-by-Side Image Views - BETTER!')
    f.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()


    img1 = plt.imread('photos/dog.jpg')
    img2 = plt.imread('photos/dog.jpg')

    NUM_ROWS = 1
    IMGs_IN_ROW = 2
    f, ax = plt.subplots(NUM_ROWS, IMGs_IN_ROW, figsize=(16, 6))

    ax[0].imshow(img1)
    ax[1].imshow(img2)

    ax[0].set_title('NO Blue Dog')
    ax[1].set_title('Happy Dog -- or, maybe not!')

    title = ('Side-by-Side Image Views - BETTER!')
    f.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()

    img_dog_large = cv.imread('photos/dog.jpg')

    plt.title('Large Dog - Note: pixel dimensions', fontweight = "bold")
    plt.imshow(cv.cvtColor(img_dog_large, cv.COLOR_BGR2RGB))
    plt.show()

    resized_dog = rescaleFrame(img_dog_large)
    plt.title('Resized Dog - Note: pixel dimensions', fontweight = "bold")
    plt.imshow(cv.cvtColor(resized_dog, cv.COLOR_BGR2RGB))
    plt.show()

    height = 480 # np rows
    width = 640 #np cols
    num_colors = 3 # np channels (B, G, R channels/colors)

    # np.zeros: Returns new array of given shape and type, filled with zeros.
    # a. display blank image
    blank_image = np.zeros((height, width, num_colors), dtype='uint8')
    plt.title('Blank Image', fontweight="bold")
    plt.imshow(blank_image)
    plt.show()

    # b. color image (BGR values)
    blank_image[:] = 255, 0, 0
    plt.title('Blue', blank_image)
    plt.imshow(blank_image)
    plt.show()

    # c. color only range of pixels (red square in blue image)
    blank_image[100:200, 300:400] = 0, 0, 255
    plt.title('Blue w/ Red Square', blank_image)
    plt.imshow(blank_image)
    plt.show()

    # d. draw rectangle (img, start_point, end_point, color, thickness)
    cv.rectangle(blank_image, (0, 0), (200, 200), (0, 255, 0), thickness = 2)
    plt.title('Rectangle', blank_image)
    plt.show()

    # e. draw rectangle w/ filled color (same as thickness = -1)
    cv.rectangle(blank_image, (0, 0), (200, 200), (0, 255, 0), thickness = cv.FILLED)
    plt.title('Rectangle Filled', blank_image)
    plt.imshow(blank_image)
    plt.show()

    # here, using ratio of height and width
    # Note: integer division operator // (only keeps whole numbers)
    cv.rectangle(blank_image, (0, 0), (blank_image.shape[1] // 4, blank_image.shape[0] // 4),
                    (255, 255, 255), thickness = -1)
    plt.title('Rectangle Filled Ratio', blank_image)
    plt.imshow(blank_image)
    plt.show()

    # f. draw a circle (img, center, radius, color, thickness)
    cv.circle(blank_image, (blank_image.shape[1] // 2, blank_image.shape[0] // 2), 30,
                (0, 0, 0), thickness = 3)
    plt.title('Circle', blank_image)
    plt.imshow(blank_image)
    plt.show()

    # g. draw line (img, start_point, end_point, color, thickness)
    cv.line(blank_image, (blank_image.shape[1], blank_image.shape[0]), (blank_image.shape[1] // 2, blank_image.shape[0] // 2),
                (255, 255, 255), thickness = 1)
    plt.title('Line', blank_image)
    plt.imshow(blank_image)
    plt.show()

    # h. write text (img, text, origin, fontFace, fontScale, color, thickness)
    cv.putText(blank_image, 'Hello World!',
                (blank_image.shape[1] // 2, blank_image.shape[0] // 2), cv.FONT_HERSHEY_SCRIPT_COMPLEX, 1.5, (0, 255, 0), thickness = 2)
    plt.title('Text', blank_image)
    plt.imshow(blank_image)
    plt.show()
    cv.waitKey(0)

# resize/rescale images
# function accepts frame, and scale value (here, 50%)
def rescaleFrame(frame, scale=.50):
    # works for images, existing videos, and live video
    width = int(frame.shape[1] * scale) # convert float to integer
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    # resize frame to specific dimensions (resampling using pixel area relation)
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)
    
def changeRes(width, height):
    # *however*, only works for *live* video
    capture.set(3, width)
    capture.set(4, height)