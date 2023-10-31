function croppedTag = AprulTag(input_img)
    I = im2gray(imread(input_img));
    
    Tag = im2gray(imread("aprilTag.jpeg"));

    montage({I, Tag});

    tagFamily = "tagStandard52h13";

    [id, loc, detectedFamily] = readAprilTag(I, tagFamily);

    for idx = 1:length(id)
        % Display the ID and tag family
        disp("Detected Tag ID, Family: " + id(idx) + ", " + detectedFamily(idx));

        % Get the corner coordinates for the detected AprilTag
        corners = loc(:, :, idx);

        % Calculate the bounding box for the AprilTag
        min_x = min(corners(:, 1));
        max_x = max(corners(:, 1));
        min_y = min(corners(:, 2));
        max_y = max(corners(:, 2));

        % Crop the AprilTag from the input image
        croppedTag = I(min_y:max_y, min_x:max_x);
        % Display the cropped AprilTag
    end
    imshow(croppedTag);
end
