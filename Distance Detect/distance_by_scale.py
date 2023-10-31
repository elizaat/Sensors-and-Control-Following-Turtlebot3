import cv2

def distance_by_scale():
    from crop_april_tag import crop_april_tag
    # Load the input image (example10.jpg)
    inpict = cv2.imread('example10.jpg')
    # Repeat the image to create a 4-frame RGB image
    inpict = cv2.repeat(inpict, 1, 1, 4)
    rows, cols, chans = inpict.shape
    #midpoint = cols // 2
    midpoint = 1500
    print("midpoint")
    ex_img1 = crop_april_tag('example10.jpg')
    ex_img2 = crop_april_tag('example9.jpg')

    # Load and convert both input images to grayscale
    I1gs = cv2.imread(ex_img1, cv2.IMREAD_GRAYSCALE)
    I2gs = cv2.imread(ex_img2, cv2.IMREAD_GRAYSCALE)
    direction = 0
    initial_distance = 10

    # Calculate the number of pixels in both images
    numpixels_1 = I1gs.size
    numpixels_2 = I2gs.size

    # Calculate the change in pixel size as a ratio
    image_difference_ratio = numpixels_2 / numpixels_1

    # Conditional statement to determine if the leaderbot is reversing
    if image_difference_ratio > 1:
        # Change the scale to suit the new direction
        image_difference_ratio = numpixels_1 / numpixels_2
        # Change the direction variable accordingly
        direction = 1

    # Calculate the distance value needed to move based on the ratio
    distance_increase = initial_distance * image_difference_ratio
    # Set the final distance value
    final_distance = distance_increase + initial_distance

    # Load 'left_edge.mat' and retrieve 'x_Marker'
    x_Marker =  1000;

    tag_pos = x_Marker

    if tag_pos > midpoint + 100:
        turn = 1
        straight = 0
        print("right")
    elif tag_pos < midpoint - 100:
        turn = 0
        straight = 0
        print("left")
    elif midpoint - 100 < tag_pos < midpoint + 100:
        straight = 1
        print("straight")

