function distancebyScale()

    inpict = imread('example9.jpg');
    % a 4-frame RGB image
    inpict = repmat(inpict,[1 1 1 4]);
    % the last output of size() does not refer to the size of dim3
    % the last output always refers to the product of all remaining sizes
    [rows, cols, chans] = size(inpict);
    midpoint = cols / 2; 
    
    %converts both inputed images to greyscale 
    I1gs = AprulTag('example10.jpg');
    I2gs = AprulTag('example9.jpg');
    %sets the direction of motion of the Turtlebot
    direction = 0;
    initalDistance = 10;
    
    %calculates the number of pixels in both images
    numpixels_1 = size(I1gs, 1) * size(I1gs, 2);  
    numpixels_2 = size(I2gs, 1) * size(I2gs, 2);
    
    
    %calculates the change in pixel size as a ratio
    imageDifferenceRatio = numpixels_2 / numpixels_1;
    
    %conditional statement to determine if the leaderbot is reversing
    if imageDifferenceRatio > 1 
        %changes the scale to suit the new direction
        imageDifferenceRatio = numpixels_1 / numpixels_2;
        %changes the direction variable acccordingly
        direction = 1;
    
    %calcuates the distance value need to move based upon the ratio
    distanceIncrease = initalDistance * imageDifferenceRatio;
    %sets the final distance value
    finalDistance = distanceIncrease + initalDistance;
    finalDistance
    direction

    load('left_edge.mat', 'x_Marker');
    
    tagPos = x_Marker;

    if tagPos > midpoint + 100 
        turn = 1;
        straight = 0;
        fprintf("right");
    elseif tagPos < midpoint - 100
        turn = 0; 
        straight = 0;
        fprintf("left");
    elseif tagPos > midpoint - 100 & tagPos < midpoint + 100
        straight = 1;
        fprintf("straight");
    end

end
