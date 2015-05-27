## video-processor

split input video to png images, processing it with OpenCV, join to output video (ffmpeg keys in config.py)

<b>How to use</b>:<br>
python2.7 main.py video/in.avi - for filtering
<br>
python2.7 dark.py video/dark.avi - for dark.png generation

<br>
<b>Available filters:</b><br>
1) crop filter<br>
CropFilter(fromX, fromY, toX, toY)<br>
<br>
2) dark filter<br>
DarkFilter(darkImgFilename)<br>
you can generate dark.png with dark.py<br>
<br>
3) gaussian filter<br>
GaussianFilter(pixelsX, pixelsY)<br>
<br>
4) median filter<br>
MedianFilter(kSize)<br>
<br>
6) moving average filter<br>
MovingAverageFilter(pixelsForX, pixelsForY)<br>
<br>
5) pseudo color filter<br>
PseudoColorFilter()<br>
working with COLORMAP_PINK
<br>
<br>
<b>Available image processors:</b><br>
1) DiffPrevImageProcessor<br>
calculate absolute difference between images<br>
<br>
2) DiffMovingAverageDarkImageProcessor<br>
calculate absolute difference between image and same image with moving average<br>
<br>
<br>
<b>Available video processors:</b><br>
1) DefaultVideoProcessor<br>
default work<br>
<br>
2) DarkGenerationVideoProcessor<br>
dark.png generation<br>
<br>
