Name: Pranav Konduru
Class: EE 104
Lab 8: Using Yolov5 to Identify objects

Video link for Yolov5 Challenge: https://youtu.be/6DPVud1udRw 
Video link for Dance Challenge: https://youtu.be/zI2w8GE-pf4

***MAKE SURE THAT THE FOLLOWING PYTHON MODULES ARE INSTALLED using pip install "library name"***

For Yolov5


tensorflow
keras
h5py
Matplotlib
numpy

For Dance Challenge

pygame
pgzero


 1. Training new class (Yolov5)
*******************************
	- Recommend moving yolov5 to main directory (C drive)
	- Used ModifiedOpenLabelling for training images
	- Followed steps for training here: https://wandb.ai/onlineinference/YOLO/reports/Collect-and-Label-Images-to-Train-a-YOLOv5-Object-Detection-Model-in-PyTorch--VmlldzoxMzQxODc3
	- Added trained images with weights by moving images ModifiedOpenLabelling to train2017 in images
	and weight box text files to train 2017 in labels
		- Ran again to split python yolov5_ee104_split_train_val_files.py
 2. Recognize new class (Yolov5)
********************************
	- Need to train large dataset (about 30) to have object detected
		- Trained about 40 images for object to get detected
	

3. Game Development - Dance Challenge
*************************************
	

	
             
