function distancebyScale()

%converts both inputed images to greyscale 
I1gs = AprulTag('example8.jpg');
I2gs = AprulTag('example7.jpg');
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
end
