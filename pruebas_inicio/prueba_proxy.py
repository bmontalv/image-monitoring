#!/usr/bin/python

import numpy as np
import cv2
import jderobot

#include <Ice/Ice.h>
#include <jderobot/camera.h>
#include <visionlib/colorspaces/colorspacesmm.h>
#include "viewer.h"


import jderobot
import Ice

#camara = cv2.VideoCapture(0)
#camara.Camera.Proxy=cameraA:default -h 0.0.0.0 -p 9999

print "hola"
try:
	communicator = Ice.initialize();
	print "Antes de proxy"
	proxy = communicator.stringToProxy('cameraA:default -h 0.0.0.0 -p 9999');
	print "despues de proxy"
	
	cprx = jderobot.CameraPrx.checkedCast(proxy);
	print "despues de cprx"
	
	#camRGB = jderobot.CameraClient(communicator,"RGB8");
	#data = jderobot.ImageDataPtr;
	#data = cprx.getImageData(colorspaces.ImageRGB8.FORMAT_RGB8.get());
	#rgb = cv2.VideoCapture(cprx);
	#cv2.imshow('frame', cprx);
except ValueError:
	print "ERROR"
		
