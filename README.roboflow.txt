
Bangla License Plate Detection - v1 2022-12-26 11:38pm
==============================

This dataset was exported via roboflow.com on December 30, 2022 at 2:38 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

It includes 2640 images.
License-plates are annotated in YOLO v3 Darknet format.

The following pre-processing was applied to each image:
* Auto-orientation of pixel data (with EXIF-orientation stripping)
* Resize to 640x640 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* 50% probability of horizontal flip
* Equal probability of one of the following 90-degree rotations: none, clockwise, counter-clockwise
* Randomly crop between 0 and 58 percent of the image
* Random rotation of between -18 and +18 degrees
* Random Gaussian blur of between 0 and 1 pixels
* Salt and pepper noise was applied to 7 percent of pixels


