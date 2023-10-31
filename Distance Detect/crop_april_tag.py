import cv2

def crop_april_tag(input_img):
    # Load the input image
    I = cv2.imread(input_img, cv2.IMREAD_GRAYSCALE)

    # Load the AprilTag image (tagStandard52h13.jpg)
    Tag = cv2.imread("aprilTag.jpeg", cv2.IMREAD_GRAYSCALE)

    # Display the input image and the AprilTag image
    cv2.imshow("Input Image", I)
    cv2.imshow("AprilTag", Tag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Create an AprilTag detector
    detector = cv2.aruco.Dictionary_get(cv2.aruco.DICT_6X6_250)
    parameters = cv2.aruco.DetectorParameters_create()

    # Detect AprilTags in the input image
    corners, ids, rejectedImgPoints = cv2.aruco.detectMarkers(I, detector, parameters=parameters)

    for i in range(len(ids)):
        # Display the detected Tag ID
        print(f"Detected Tag ID: {ids[i][0]}")

        # Get the corner coordinates for the detected AprilTag
        tag_corners = corners[i][0]

        # Calculate the bounding box for the AprilTag
        min_x = int(min(tag_corners[:, 0]))
        max_x = int(max(tag_corners[:, 0]))
        min_y = int(min(tag_corners[:, 1]))
        max_y = int(max(tag_corners[:, 1]))

        # Crop the AprilTag from the input image
        croppedTag = I[min_y:max_y, min_x:max_x]

        # Display the cropped AprilTag
        cv2.imshow("Cropped AprilTag", croppedTag)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # Save the x-coordinate of the first corner
    x_Marker = corners[0][0][0][0]
    cv2.imwrite("Cropped_AprilTag.jpg", croppedTag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return croppedTag

# Call the function with the input image path
croppedTag = crop_april_tag("example10.jpg")
